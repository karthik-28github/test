from sqlalchemy import Column,String,Integer,Float
from database1 import Base

class EmployeeDetails(Base):
    __tablename__='mcs'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    phone=Column(Integer)
    salary=Column(Float)


