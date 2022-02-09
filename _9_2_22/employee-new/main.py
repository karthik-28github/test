from fastapi import FastAPI,Depends
from typing import List
import uvicorn
from scemas import Employee,EmpBody
from utilities import get_db
from views import add_employee_service,get_all
from database1 import engine
import models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


app=FastAPI()

@app.post('/addemployee',response_model=EmpBody)
def add_employee(e:Employee,db:Session = Depends(get_db)):
    id=e.id
    name=e.name
    phone=e.phone
    salary=e.salary
    return add_employee_service(id,name,phone,salary,db)

@app.get('/seeall')
def all1(db:Session = Depends(get_db)):
    return get_all(db)

# @app.put('/seeall')
# def alter(id:int,name:Employee.name,db:Session = Depends(get_db)):
#     return alter(id,name,db)


if __name__=="__main__":
    uvicorn.run(app,debug=True)
