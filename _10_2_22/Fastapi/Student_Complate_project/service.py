from utilities import add_student_utilities,show_student_utilities,\
    update_student_utilities,delete_student_record_utilities


def add_student_service(id,name,marks1,marks2,marks3,marks4,marks5,marks6,db):
    sum=0
    avg=0
    chance=False
    status=''
    if marks1 and marks2 and marks3:
        sum = marks1 + marks2 + marks3
        avg = sum / 3
    if marks4:
        sum = marks1 + marks2 + marks3 + marks4
        avg = sum / 4
        if marks5:
            sum = marks1 + marks2 + marks3 + marks4 + marks5
            avg = sum / 5
            if marks6:
                sum = marks1 + marks2 + marks3 + marks4 + marks5 + marks6
                avg = sum / 6

    if avg >= 90.0:
        status='distinction'
    elif avg== 75.0:
        status="just pass"
    elif avg >= 75.0 and avg <= 90.0:
        status='average'
    elif avg<75:
        status="fail"
        chance=True

    return add_student_utilities(id,name,marks1,marks2,marks3,marks4,marks5,marks6,
                                     avg,status,chance,db)

def show_student_service(db):
    return show_student_utilities(db)

def update_student_service(s,db):
    return update_student_utilities(s,db)

def delete_student_record_services(id,db):
    return delete_student_record_utilities(id,db)

