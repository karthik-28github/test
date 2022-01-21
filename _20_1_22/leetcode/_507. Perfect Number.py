#507. Perfect Number
#A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

#Given an integer n, return true if n is a perfect number, otherwise return false.

num=int(input("enter the number"))
lst=[]
for i in range(1,num):
    if num%i==0:
        lst.append(i)
sum1=sum(lst)
print(lst)

if num==sum1:
    print("the sum of",lst,"is =",sum1)
    print("so the number which you have givin is a perfect number")
