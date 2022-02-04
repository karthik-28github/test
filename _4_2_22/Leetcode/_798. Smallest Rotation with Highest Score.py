#798. Smallest Rotation with Highest Score


lst=[3,4,5,1,2,0]
lst1=[]
max1=0
for i in range(len(lst)):
    lst=lst[1:]+lst[:1]
    lst1.append(lst)
    max1=max(max1,lst[0])

print("The max number in the list givin is",max1)

print(lst1)
for i in lst1:
    if i[0]==5:
        print(i)

