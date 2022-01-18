#finds a number which is alone in the list or array

lst1=[1,2,3,4,5,6,1,2,3,6]
lst2=[]


for i in lst1:
    if lst1.count(i)>1:
        pass
    else:
        lst2.append(i)


print("the value available in this list is a single number",lst2)
