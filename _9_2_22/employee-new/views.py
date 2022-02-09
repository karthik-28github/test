from utilities import add_employee_database,get_all_data

def add_employee_service(id,name,phone,salary,db):
    return add_employee_database(id,name,phone,salary,db)

def get_all(db):
    return get_all_data(db)

# def alter(id,name,db):
#     return update(id,name,db)