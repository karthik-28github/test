
from database1 import SessionLocal
import models,scemas

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


def add_employee_database(id,name,phone,salary,db):
    new_user=models.EmployeeDetails(id=id,name=name,phone=phone,salary=salary)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "data added Successfully"

def get_all_data(db):
    new_user=db.query(models.EmployeeDetails)#.filter(models.EmployeeDetails.id==1).first()
    return new_user
# def update(id,name,db):
#     new_user=db.query(models.EmployeeDetails).filter(models.EmployeeDetails.id==id).first()
#     new_user.name=name
#     db.commit()
#     db.refresh(new_user)
#     return "updated"