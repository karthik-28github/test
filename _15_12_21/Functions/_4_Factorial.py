#factorial of a givin number
def fac(b):
    fact=1
    for i in range(2,b+1):
        fact=fact*i
    print(fact)

a=int(input("enter the number "))
fac(a)