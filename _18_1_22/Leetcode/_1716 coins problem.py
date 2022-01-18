#

n=int(input("enter the value of n"))
m=7
while n!=0:
    if n>=7:
        n=n//7
        for i in range(8):
            print(i,end="")
    else:
        for i in range(len(n)):
            print(i)