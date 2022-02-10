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
