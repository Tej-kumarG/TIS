import time
from typing import Optional

from fastapi import HTTPException, APIRouter
import asyncio
# from src.database import Database
from app.services.exa_api import ExaAPI
from app.services.llm_processor import LLMProcessor
from app.utils.prompts import university_system_prompt, course_system_prompt, \
 university_name_system_prompt, scholarship_prompt, course_scholarship_prompt

exa = ExaAPI()
llm_processor = LLMProcessor()
router = APIRouter(prefix="", tags=["University"])

@router.post("/university")
async def get_university_details(university_name: str, country_name: str):

    try:
        university_data_raw = exa.fetch_university_data(
            f'All available details about the {university_name} in {country_name}.'
        )
        university_data =await llm_processor.process_data(university_system_prompt, university_data_raw)

        return university_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing {university_name}: {e}")

@router.post("/course")
async def get_course_details(course_name: str,country_name: str, course_type:Optional[str] = None):
    try:
        if course_type:
            query = f"Fetch all the available {course_name} course details in {country_name} for {course_type} programs."
        else:
            query = f"Fetch all the available {course_name} course details in {country_name} for program types such as Bachelor's, Master's and Ph.D."

        course_data = exa.fetch_university_data(query)
        course_list = await llm_processor.process_course_data(course_system_prompt, course_data)
        return course_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching universities for course {course_name}: {e}")


@router.post("/university_details")
async def get_university(course_name: str, country_name: str, course_type: Optional[str] = None):
    try:
        if course_type:
            query = f"Fetch all the universities' names that offer the {course_type} program in {course_name} in {country_name}."
        else:
            query = f"Fetch all the universities' names that offer {course_name} in {country_name} for all program types such as Bachelor's, Master's and Ph.D."
        university_data = exa.fetch_university_data(query)
        university_list = await llm_processor.process_university_data(university_name_system_prompt, university_data)
        return university_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching universities for university: {e}")

@router.post("/course_with_scholarship")
async def get_course_scholarship_details(university_name: str, course_name:str, country_name: str, course_type: Optional[str] = None):
    try:
        if course_type:
            query = (
                f"Fetch all the details of the {course_name} for the {course_type} program offered by the {university_name} in {country_name}."
            )
        else:
            query = (
                f"Fetch all the details of the '{course_name}' for Bachelors and Masters offered by the {university_name} in {country_name} "
            )
        scholarship_data = exa.fetch_university_data(query)
        scholarship_list = await llm_processor.process_scholarship_course_data(course_scholarship_prompt, scholarship_data)
        return scholarship_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching scholarships for university {university_name}: {e}")


@router.post("/scholarship_details")
async def fetch_scholarship_details(course_name: str, country_name: str, course_type: Optional[str] = None):
    try:
        if course_type:
            query = (
                f"Fetch all the scholarships provided by different universities "
                f"offering the {course_type} program in {course_name} in {country_name}."
            )
        else:
            query = (
                f"Fetch all the scholarships provided by different universities "
                f"offering {course_name} in {country_name} across all program types."
            )
        scholarship_data = exa.fetch_university_data(query)
        scholarship_dict = await llm_processor.scholarship_data_process(scholarship_prompt, scholarship_data)
        # db_service.store_scholarship_data(university_name, scholarship_name, scholarship_dict)
        return scholarship_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing: {e}")

