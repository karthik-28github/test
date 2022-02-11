from pydantic import BaseModel


class Student(BaseModel):
    id:int
    name:str
    marks1:int
    marks2:int
    marks3:int
    marks4:int
    marks5:int
    marks6:int

class update_Student(BaseModel):
    id:int
    name:str

class Student_failed(BaseModel):
    marks1:int
    marks2:int
    marks3:int
    marks4:int
    marks5:int
    marks6:int

class Student_revaluation(BaseModel):
    id:int
    marks1:int
    marks2:int
    marks3:int
    marks4:int
    marks5:int
    marks6:int

class response(BaseModel):
    id: int
    marks1: int
    marks2: int
    marks3: int
    marks4: int
    marks5: int
    marks6: int
    avg=float
    status:str
    chance:bool

class csv_upload(BaseModel):
    id: int
    name: str
    marks1: int
    marks2: int
    marks3: int
    marks4: int
    marks5: int
    marks6: int