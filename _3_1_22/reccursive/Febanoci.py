#Febanocii series
def febanoci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return (febanoci(n-1)+febanoci(n-2))




num=int(input("enter the number "))
for i in range(num):
    print(febanoci(i))