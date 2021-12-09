# square and cube symbol in the area of a rectangle and volume of a cylinder
import math
try:
    a=int(input("enter the number to calculate"))
    if a==0:
        raise ValueError
    if a>0 :
        print("the square of ",a,"is",a*a)
        print("cube of a is",a**3)
        print("sqrt of s is", math.sqrt(a))
except ValueError:
    print("value must not be zero")

