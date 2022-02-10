from database import engine
from fastapi import FastAPI,Depends
from models import StudentDetails
from schemas import Student,update_Student
from sqlalchemy.orm import Session
from utilities import get_db
from service import add_student_service,show_student_service,\
    update_student_service,delete_student_record_services
import uvicorn
import models

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/add_student')
def add_student(s:Student,db:Session=Depends(get_db)):
    id=s.id
    name=s.name
    marks1=s.marks1
    marks2=s.marks2
    marks3=s.marks3
    marks4=s.marks4
    marks5=s.marks5
    marks6=s.marks6
    return add_student_service(id,name,marks1,marks2,marks3,marks4,marks5,marks6,db)

@app.get('/show_students')
def show_student(db:Session=Depends(get_db)):
    return show_student_service(db)

@app.put('/update_student_name')
def update_student_name(s:update_Student,db:Session=Depends(get_db)):
    return update_student_service(s,db)

@app.delete("/delete_student")
def delete_student_record(id:int,db:Session=Depends(get_db)):
    return delete_student_record_services(id,db)

if __name__=="__main__":
    uvicorn.run(app,debug=True)