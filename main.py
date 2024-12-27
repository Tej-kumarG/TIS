from fastapi import FastAPI

from app.api import university

app = FastAPI()
app.include_router(university.router)


