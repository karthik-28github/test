from database import insert_data
from utils import database_retrive, database_retrive_one

def service_insert(new_user,db):
    if new_user.eid %2 == 0:
        return insert_data(new_user,db)
    else:
        return "Fail"

def service_retrive(db):
    return database_retrive(db)

def service_retrive_one(id,db):
    if id > 10:
        return database_retrive_one(id,db)
    else:
        return "user is not available"