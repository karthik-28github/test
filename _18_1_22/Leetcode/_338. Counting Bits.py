#count number of 1's in the binary value

n=int(input("enter the value of n"))
lst=[]
for i in range(n+1):
    a=bin(i)
    count=a.count("1")
    lst.append(count)
print(lst)

