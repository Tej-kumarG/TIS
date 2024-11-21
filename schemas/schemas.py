from typing import Optional, List, TypedDict, Dict, Annotated

from typing_extensions import TypedDict
from decimal import Decimal


class CourseHeyDetails(TypedDict):
    course_id: str
    course_name: str
    course_duration: Optional[str] 
    course_level: str
    course_description: str
    specializations: Optional[str] 
    entry_requirements: Optional[str] 
    assessment_methods: Optional[str]
    teaching_methods: str
    accreditation: Optional[str] 
    tuition_fee: Optional[str] 
    application_deadline: Optional[str] 
    career_outcomes: Optional[str] 
    course_location: str
    contact_information: Optional[str]

class UniversityData(TypedDict):
    university_id: str
    university_name: str
    university_url: str
    university_location: str
    university_founded: int
    university_type: str
    number_of_colleges: int
    courses: List[str]
    student_population: int
    international_students_percentage: Decimal
    student_gender_distribution: Optional[str] 
    university_ranking_global: int
    university_ranking_national: int
    notable_alumni: List[str]
    university_research_output: str
    number_of_nobel_laureates: int
    university_press: str
    university_museums: List[str]
    accommodation_options: str
    average_tuition_fee_undergraduate: str
    average_tuition_fee_postgraduate: Optional[str] 
    living_cost_estimate: Optional[str] 
    scholarships_available: str
    admission_requirements_general: str
    language_requirements: str
    sports_facilities: List[str]
    student_organizations: str
    campus_life_description: str
    university_facilities: str

class UniversityResponse(TypedDict):
    result: UniversityData

class CourseResponse(TypedDict):
    university_names: List[str]

class AdmissionRequirements(TypedDict):
    Academic: List[str]
    English: List[str]
    Other: List[str]

class CourseDetails(TypedDict):
    course_id: int
    discipline_id: str
    course_name: str
    course_description: str
    university_url: str
    university_id: int
    university_name: str
    university_location: str
    course_tuition_fees_yearly: str
    course_duration: str
    course_start_date: str
    course_dead_date: Optional[str]
    course_type: str
    minimum_living_cost: Annotated[str, "Minimum living cost required for the course in the particular country"]
    maximum_living_cost: Annotated[str, "Maximum living cost required for the course in the particular country"]
    gpa_score: Optional[str]
    gpa_scale: Optional[str]
    TOEFL: Optional[int]
    PTE: Optional[int]
    IELTS: Optional[Decimal]
    DUOLINGO: Optional[int]
    programming_structure: List[str]
    about_the_program: str
    overview_ref_grp: str
    admission_requirements: AdmissionRequirements
    work_permit: Dict
    id: str

class CourseDetailsResponse(TypedDict):
    course_details  : List[CourseDetails]


class ScholarshipDetails(TypedDict):
    scholarship_url: str
    description: str
    benefits: str
    scholarship_coverage: str
    eligibility: str
    discipline: str
    location: str
    nationality: List[str]
    study_experience: str
    age: str
    application_deadline: Optional[str]
    application_details: str
    id: str
    name: str
    basis: str
    provided_by: str
    provided_fund: str
    deadline: str

class ScholarshipDetailsResponse(TypedDict):
    scholarship_details: List[ScholarshipDetails]

class UniversityNameResponse(TypedDict):
    university_details: List[UniversityData]

class CourseNameScholarship(TypedDict):
    course_id: int
    discipline_id: str
    course_name: str
    course_description: str
    course_tuition_fees_yearly: str
    course_duration: str
    course_start_date: str
    course_dead_date: Optional[str]
    course_type: str
    scholarships_available: List[str]
    university_url: str
    university_id: int
    university_name: str
    university_location: str

class CourseScholarship(TypedDict):
    course_details: List[CourseNameScholarship]