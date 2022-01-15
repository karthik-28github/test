#find the duplicate number in the list
#print the number and pop the element from the list
lst1=[]
lst2=[]
lst=[1,2,3,4,5,6,6,6,7,8,9,9]

for i in lst:
    if i not in lst1:
        lst1.append(i)
    else:
        lst2.append(i)

print("given list is",lst)
print("the list with out duplicate values is",lst1)
print("the set of duplicate values from the list is ",lst2)