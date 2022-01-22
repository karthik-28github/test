#896. Monotonic Array

n=int(input("enter how many elements"))
lst=[]
flag=False
asc=False
for i in range(n):
    ele=int(input("enter the element"))
    lst.append(ele)
for i in range(1,len(lst)):
    if lst[i]>lst[i-1]:
        flag=True
        asc=True
    elif lst[i]<lst[i-1]:
        flag=True
        asc=False
    else:
        flag=False
if flag:
    if asc:
        print("the givin list is ascending order")
    else:
        print("the givin list is decending order")
else:
    print("the list is not givin in either ascending and decending order")