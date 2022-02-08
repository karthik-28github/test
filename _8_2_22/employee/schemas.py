from pydantic import BaseModel

class Employee(BaseModel):
    ename : str
    eid : int
    eloc : str