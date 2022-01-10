#eleminate the max number first
lst1=[]
n=int(input("enter the value of n"))
for i in range(n):
    j=int(input("enter the number"))
    lst1.append(j)



while len(lst1)!=1:
    max1 = 0
    for i in range(len(lst1)):
        max1=max(lst1[i],max1)
    print("the max number is",max1)
    lst1.remove(max1)

print(lst1)
