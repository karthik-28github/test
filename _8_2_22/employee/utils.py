from database import SessionLocal
import models
from models import Employee_model
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def database_retrive(db):
    user_data = db.query(models.Employee_model)
    response = {}
    for each in user_data:
        response[each.ename] = each.ename
        response[each.ename+' id'] = each.eid
        response[each.ename + ' location'] = each.eloc
    return response

def database_retrive_one(id,db):
    user_data = db.query(Employee_model).filter(Employee_model.eid == id).first()
    response = {}
    response['name'] = user_data.ename
    response['id'] = user_data.eid
    response['location'] = user_data.eloc
    return response