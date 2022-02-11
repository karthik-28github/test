from database import engine
from fastapi import FastAPI,Depends,File,UploadFile
from schemas import Student, update_Student, Student_failed,Student_revaluation,response
from sqlalchemy.orm import Session
from utilities import get_db
from service import add_student_service,show_student_service,\
    update_student_service,delete_student_record_services,update_for_failed_service,\
revaluation_for_student_service
import uvicorn
import models

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/csv_upload')
def csv_upload(myfile: UploadFile,db:Session=Depends(get_db)):
    list2 = []
    encode = 'utf-8'
    str1 = myfile.file.read().decode(encode)
    for x in str1.split('\r\n'):
        list2.append(x)

    list1=[]
    for x in list2:
        if x:
            list1.append(x.split(','))

    for i in list1:
        id=int(i[0])
        name=i[1]
        marks1=int(i[2])
        marks2=int(i[3])
        marks3=int(i[4])
        marks4=int(i[5])
        marks5=int(i[6])
        marks6=int(i[7])
        add_student_service(id, name, marks1, marks2, marks3, marks4, marks5, marks6, db)
    return "csv data added successfully"


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

@app.get('/show_students',response_model=response)
def show_student(db:Session=Depends(get_db)):
    return show_student_service(db)

@app.put('/update_student_name')
def update_student_name(s:update_Student,db:Session=Depends(get_db)):
    return update_student_service(s,db)

@app.delete("/delete_student")
def delete_student_record(id:int,db:Session=Depends(get_db)):
    return delete_student_record_services(id,db)

@app.put('/update_for_failed')
def update_for_failed(s:Student_failed,db:Session=Depends(get_db)):
    marks1=s.marks1
    marks2=s.marks2
    marks3=s.marks3
    marks4=s.marks4
    marks5=s.marks5
    marks6=s.marks6
    return update_for_failed_service(marks1,marks2,marks3,marks4,marks5,marks6,db)
@app.put('/update_revaluation')
def revaluation_for_student(s:Student_revaluation,db:Session=Depends(get_db)):
    id=s.id
    marks1 = s.marks1
    marks2 = s.marks2
    marks3 = s.marks3
    marks4 = s.marks4
    marks5 = s.marks5
    marks6 = s.marks6

    return revaluation_for_student_service(id,marks1,marks2,marks3,marks4,marks5,marks6,db)

if __name__=="__main__":
    uvicorn.run(app,debug=True)