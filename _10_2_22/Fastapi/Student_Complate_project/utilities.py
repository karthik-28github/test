from database import SessionLocal
import models,schemas

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


def add_student_utilities(id,name,marks1,marks2,marks3,marks4,marks5,marks6,avg,status,chance,db):
    new_student=models.StudentDetails(id=id,name=name,marks1=marks1,marks2=marks2,
                                      marks3=marks3,marks4=marks4,marks5=marks5,marks6=marks6,
                                      avg=avg,status=status,chance=chance)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return "Student data added Successfully"

def show_student_utilities(db):
    all_students=db.query(models.StudentDetails).all()
    response=[]
    for each in all_students:
        '''response.append([["id=",each.id,each.name,each.marks1,each.marks2,
        each.marks3,each.marks4,each.marks5,each.marks6,each.avg,each.status,each.chance]])'''
        # response[id] = each.id
        # response[each.name] = each.name
        # response[each.marks1 ] = each.marks1
        # response[each.marks2 ] = each.marks2
        # response[each.marks3 ] = each.marks3
        # response[each.marks4 ] = each.marks4
        # response[each.marks5 ] = each.marks5
        # response[each.marks6 ] = each.marks6
        # response[each.percentage]=each.percentage
        # response[each.status]=each.status
        # response[each.chance]=each.chance
    return all_students

def update_student_utilities(s,db):

    student=db.query(models.StudentDetails).filter(models.StudentDetails.id==s.id).first()
    student.name=s.name
    db.commit()

    return f"name successfully updated to {s.name}"

def delete_student_record_utilities(id,db):
    remove=db.query(models.StudentDetails).filter(models.StudentDetails.id==id).delete
    db.commit()
    return f"the data belongs to student_id {id} has been deleted"
