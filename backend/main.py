from fastapi import FastAPI
from pydantic import BaseModel


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str


class StudentUpdateSchema(BaseModel):
    first_name: str
    last_name: str


app = FastAPI()

@app.post("/students")
async def create_student(student: StudentCreateSchema):
    return student

@app.get("/student/{id}")
async def get_student(id: int):
    pass

@app.get("/")
async def root():
    return {"message": "JD"}