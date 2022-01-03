#Factorial of a number
def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n*facto(n-1)




num=int(input("enter the number"))
print("the factorial of ",num,"is",facto(num))