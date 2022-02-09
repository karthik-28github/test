from unicodedata import name
from pydantic import BaseModel


class Employee(BaseModel):
    id:int
    name:str
    phone:int
    salary:float

class EmpBody(BaseModel):
    name:str
    phone:int
    class Config:
        orm_mode=True
