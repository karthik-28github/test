#812. Largest Triangle Area
#the largest triangle that can be made by giving the values for the points

lst=[]
n=int(input("how many points"))
for i in range(n):
    lst1=[]
    for j in range(2):
        x=int(input("enter x"))
        lst1.append(x)
    lst.append(lst1)
print(lst)
max1=0
max2=0
for i in lst:
    print(i[0])
    max1=max(i[0],max1)
for j in lst:
    print(j[0])
    max2=max(j[0],max2)

print("the maximum trianle that can be drawn using the given data is","[0,",max1,"] and [",max2,"0]")
