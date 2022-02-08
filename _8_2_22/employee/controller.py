from fastapi import FastAPI, Depends
import uvicorn
from schemas import Employee
from sqlalchemy.orm import Session
from utils import get_db
from service import service_insert, service_retrive, service_retrive_one
import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.post('/insert')
def insert_data(emp : Employee, db : Session = Depends(get_db)):
    new_user = models.Employee_model(eid = emp.eid, ename = emp.ename, eloc = emp.eloc)

    return service_insert(new_user,db)

@app.get('/retrieve')
def retrieve_data(db : Session = Depends(get_db)):
    return service_retrive(db)

@app.get('/retrieve/{id}')
def retrieve_data(id:int, db : Session = Depends(get_db)):
    return service_retrive_one(id,db)


if __name__ == '__main__':
    uvicorn.run(app)