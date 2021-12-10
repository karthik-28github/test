#voter id  age must be grater than or equal to 18


age=int(input("enter the age "))
try:
    if age<18:
        raise ValueError("not valid")
    else:
        print("elegible to vote")
except ValueError as e:
    print(e)
    print("you are not eligible to cast vote")