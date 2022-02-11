from database import SessionLocal
import models,schemas

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


def add_student_utilities(id,name,marks1,marks2,marks3,marks4,marks5,marks6,avg,status,chance,db):
    try:
        new_student=models.StudentDetails(id=id,name=name,marks1=marks1,marks2=marks2,
                                          marks3=marks3,marks4=marks4,marks5=marks5,marks6=marks6,
                                          avg=avg,status=status,chance=chance)
        print(new_student.chance)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return f"Student data added Successfully  and chance is{new_student.chance}"
    except Exception as e:
        pass
def show_student_utilities(db):
    all_students=db.query(models.StudentDetails).all()
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
    oldname=student.name
    student.name=s.name
    db.commit()

    return f"name {oldname} successfully updated to {s.name}"

def delete_student_record_utilities(id,db):
    remove=db.query(models.StudentDetails).filter(models.StudentDetails.id==id).delete
    db.commit()
    return f"the data belongs to student_id {id} has been deleted"

def update_for_failed_utilities(marks1,marks2,marks3,marks4,marks5,marks6,db):
    failed=db.query(models.StudentDetails).filter(models.StudentDetails.chance==True).first()
    sum=marks1+marks2+marks3+marks4+marks5+marks6
    status=''
    avg=sum/6
    if avg >= 90.0:
        status = 'distinction'
        chance = False
    elif avg == 75.0:
        status = "just pass"
        chance = False
    elif avg >= 75.0 and avg <= 90.0:
        status = 'average'
        chance = False
    elif avg < 75:
        status = "fail"
        chance = False
    failed.marks1=marks1
    failed.marks2=marks2
    failed.marks3=marks3
    failed.marks4=marks4
    failed.marks5=marks5
    failed.marks6=marks6
    failed.avg=avg
    failed.status=status
    failed.chance=chance
    db.commit()

    return f"failed student {failed.name} has been passed successfully"

def revaluation_for_student_utilities(id,marks1,marks2,marks3,marks4,marks5,marks6,db):
    update=db.query(models.StudentDetails).filter(models.StudentDetails.id==id).first()
    str1=''
    if marks1:
        update.marks1=marks1
        str1=str1+"marks1"
    if marks2:
        str1=str1+"marks2"
        update.marks2 = marks2
    if marks3:
        str1=str1+"marks3"
        update.marks3 = marks3
    if marks4:
        str1=str1+"marks4"
        update.marks4 = marks4
    if marks5:
        str1=str1+"marks5"
        update.marks5 = marks5
    if marks6:
        str1=str1+"marks6"
        update.marks6 = marks6
    str1=str1+"has been updated"
    sum = update.marks1 + update.marks2 + update.marks3 + update.marks4 + update.marks5 + update.marks6
    status = ''
    avg = sum / 6
    if avg >= 90.0:
        status = 'distinction'
        chance = False
    elif avg == 75.0:
        status = "just pass"
        chance = False
    elif avg >= 75.0 and avg <= 90.0:
        status = 'average'
        chance = False
    elif avg < 75:
        status = "fail"
        chance = False
    update.status=status
    update.avg=avg
    update.chance=chance
    db.commit()
    return f"marks {str1} successfully"

