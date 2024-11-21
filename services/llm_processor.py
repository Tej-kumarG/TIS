import json
import os
from dotenv import load_dotenv
import tiktoken

from app.schemas.schemas import CourseDetails, UniversityData, CourseDetailsResponse, ScholarshipDetailsResponse, \
    UniversityNameResponse, CourseScholarship
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class LLMProcessor:
    def __init__(self):
        load_dotenv()
        # gemini.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.openai_api_key=os.getenv('OPENAI_API_KEY')
        # Configure Gemini API
        self.tokenizer = tiktoken.get_encoding("cl100k_base")  # Tokenizer for counting tokens

    def retrieve_dict(self,data_string):
        """Extract a JSON object from a string."""
        try:
            data_string = data_string.replace('`', "").replace('json', "")
            json_str = data_string[data_string.find('{'):data_string.rfind('}') + 1].strip()
            return json.loads(json_str) if json_str else {}
        except (json.JSONDecodeError, ValueError):
            raise ValueError("The extracted string is not a valid JSON format.")

    def _count_tokens(self, text):
        """Calculate the number of tokens in the input text."""
        return len(self.tokenizer.encode(text))

    def _calculate_price(self, input_tokens, output_tokens):
        """
        Calculate the price based on input and output tokens.
        Formula:
            Input Price:  $0.075 / 1 million tokens (for prompts <= 128k tokens)
            Output Price: $0.30 / 1 million tokens (for prompts <= 128k tokens)
        """
        input_price_per_million = 0.075
        output_price_per_million = 0.30

        input_price = (input_tokens / 1_000_000) * input_price_per_million
        output_price = (output_tokens / 1_000_000) * output_price_per_million

        return input_price + output_price

    async def course_data_process(self, prompt, course_data=None):
        llm = ChatOpenAI(model = "gpt-4o-mini", api_key=self.openai_api_key)

        formatted_data = str(course_data).replace("{", "").replace("}", "")
        prompt_temp = ChatPromptTemplate([("system",prompt),("human", f"{formatted_data}") ])
        structured = llm.with_structured_output(CourseDetails)

        few_shot_resp = prompt_temp | structured
        response = few_shot_resp.invoke({"documents": course_data})
        return response

    async def process_data(self, prompt, college_data=None):
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=self.openai_api_key)

        formatted_data = str(college_data).replace("{", "").replace("}", "")
        prompt_template = ChatPromptTemplate([("system",prompt),("human", f"{formatted_data}") ])

        structured_llm = llm.with_structured_output(UniversityData)

        few_shot_response =prompt_template | structured_llm

        response = few_shot_response.invoke({"documents": college_data})

        return response


    async def process_scholarship_data(self, prompt, scholarship_data):
        # model = gemini.GenerativeModel("gemini-1.5-flash")
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=self.openai_api_key)
        formatted_data = str(scholarship_data).replace("{", "").replace("}", "")
        prompt_template = ChatPromptTemplate([("system", prompt), ("human", f"{formatted_data}")])

        structured_llm = llm.with_structured_output(ScholarshipDetailsResponse)

        few_shot_response = prompt_template | structured_llm

        response = few_shot_response.invoke({"documents": scholarship_data})
        return response

    async def process_course_data(self, prompt, course_data):
        # model = gemini.GenerativeModel("gemini-1.5-flash")
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=self.openai_api_key)

        formatted_data = str(course_data).replace("{", "").replace("}", "")
        prompt_template = ChatPromptTemplate([("system", prompt), ("human", f"{formatted_data}")])

        structured_llm = llm.with_structured_output(CourseDetailsResponse)

        few_shot_response = prompt_template | structured_llm

        response = few_shot_response.invoke({"documents": course_data})
        return response

        # Prepare the prompt for the API
        # prompt = course_system_prompt.format(documents=university_data)

        # Calculate token count for the input prompt
        # input_tokens = self._count_tokens(prompt)
        # print(f"Input Tokens: {input_tokens}")

        # Generate the response from the API
        # response = model.generate_content(contents=prompt)
        # response = openai.Completion.create(
        #     model="gpt-4o-mini",
        #     prompt=prompt,
        #     max_tokens=1000
        # )
        # json_response = self.retrieve_dict(response.choices[0].text.strip())

        # Calculate token count for the response text
        # output_tokens = self._count_tokens(response.choices[0].text)
        # print(f"Output Tokens: {output_tokens}")

        # Calculate the total price based on token usage
        # total_price = self._calculate_price(input_tokens, output_tokens)
        # print(f"Total Price: ${total_price:.4f}")
        # Return the response text
        # return json_response

    async def process_scholarship_course_data(self, prompt, scholarship_data):
        # model = gemini.GenerativeModel("gemini-1.5-flash")
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=self.openai_api_key)
        formatted_data = str(scholarship_data).replace("{", "").replace("}", "")
        prompt_template = ChatPromptTemplate([("system", prompt), ("human", f"{formatted_data}")])

        structured_llm = llm.with_structured_output(CourseScholarship)

        few_shot_response = prompt_template | structured_llm

        response = few_shot_response.invoke({"documents": scholarship_data})
        return response

    async def process_university_data(self, prompt, college_data):
        # model = gemini.GenerativeModel("gemini-1.5-flash")
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=self.openai_api_key)

        formatted_data = str(college_data).replace("{", "").replace("}", "")
        # formatted_data = str(college_data).replace("{", "").replace("}", "")
        prompt_template = ChatPromptTemplate([("system", prompt), ("human", f"{formatted_data}")])

        structured_llm = llm.with_structured_output(UniversityNameResponse)

        few_shot_response = prompt_template | structured_llm

        response = few_shot_response.invoke({"documents": college_data})
        return response

    async def scholarship_data_process(self, prompt, scholarship_data):
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=self.openai_api_key)
        formatted_data = str(scholarship_data).replace("{", "").replace("}", "")
        prompt_template = ChatPromptTemplate([("system", prompt), ("human", f"{formatted_data}")])
        structured_llm = llm.with_structured_output(CourseScholarship)
        few_shot_response = prompt_template | structured_llm
        response = few_shot_response.invoke({"documents": scholarship_data})
        return response
