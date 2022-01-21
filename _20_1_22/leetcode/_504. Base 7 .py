#504. Base 7
#show the given numbers in the base of 7


num=int(input("enter the number "))
lst=[]
while(num>=7):
    res=num%7
    res3=num/7
    lst.append(res)
    lst.append(res3)
    res1=num/7
    num=res*7
    num=num-res1
print(lst)