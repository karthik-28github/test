#only accepts positive numbers


a=int(input("enter a number "))
try:
    if a<0:
        raise ValueError("not valid")
    else:
        print("great its a positive number")
except ValueError as e:
    print(e)
    print("you cant enter a negative number")