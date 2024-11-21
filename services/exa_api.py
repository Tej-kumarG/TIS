# exa_api.py

import os

from dotenv import load_dotenv
from exa_py import Exa

load_dotenv()


class ExaAPI:
    def __init__(self):
        self.exa = Exa(os.getenv('EXA_API_KEY'))

    def fetch_university_data(self, query):
        result = self.exa.search_and_contents(
            query,
            type="keyword",
            num_results=20,
            text=True,
            livecrawl="always"
        )
        if result:
            print(result)
            return result
        else:
            raise Exception("No data found from Exa API")

    # def fetch_course_data(self, query):
    #     result = self.exa.search_and_contents(
    #         query,
    #         type="keyword",
    #         num_results=20,
    #         text=True,
    #         livecrawl="always"
    #     )
    #     if result:
    #         print(result)
    #         return result
    #     else:
    #         raise Exception("No data found from Exa API")
    #
    # def fetch_scholarship_data(self, query):
    #     result = self.exa.search_and_contents(
    #         query,
    #         type="keyword",
    #         num_results=10,
    #         text=True,
    #         livecrawl="always"
    #     )
    #     if result:
    #         print(result)
    #         return result
    #     else:
    #         raise Exception("No data found from Exa API")
    #
    # def fetch_scholarship_details(self, query):
    #      result = self.exa.search_and_contents(
    #         query,
    #         type="keyword",
    #         num_results=20,
    #         text=True,
    #         livecrawl="always"
    #     )
    #      if result:
    #          print(result)
    #          return result
    #      else:
    #          raise Exception("No data found from Exa API")
