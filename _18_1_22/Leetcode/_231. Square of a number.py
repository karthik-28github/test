#check whether the givin number  is a sqare root  of any number
import math

n=int(input("enter a number"))

m=math.sqrt(n)

print(m)

if n%m==0:
    print("the number has a square root")
    print("the square root of",n,"is",int(m))
else:
    print("the number",n," dont a sqaure root value ")