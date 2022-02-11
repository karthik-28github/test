from sqlalchemy import Column,String,Integer,Float,Boolean
from database import Base



class StudentDetails(Base):
    __tablename__='student'
    id=Column(Integer,primary_key=True)
    name=Column(String(30),nullable=False)
    marks1=Column(Integer,nullable=False)
    marks2=Column(Integer,nullable=False)
    marks3=Column(Integer,nullable=False)
    marks4=Column(Integer,nullable=True)
    marks5=Column(Integer,nullable=True)
    marks6=Column(Integer,nullable=True)
    avg=Column(Float)
    status=Column(String(50))
    chance=Column(Boolean)

