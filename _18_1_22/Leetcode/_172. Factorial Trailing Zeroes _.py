#factorial trailing with 0

def facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n*facto(n-1)


n=int(input("enter a number to find the factorial"))
f=facto(n)
str1=str(f)
print(str1)
count=str1.count("0")
print("the result has",count,"no of 0's ")