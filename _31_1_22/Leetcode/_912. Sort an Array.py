#912. Sort an Array
#take n number of elements from the user and add that to the array
#and display the sorted array to the user
import numpy as np
n= int(input("enter the value of n"))
lst=[]

for i in range(n):
    ele=int(input("enter values"))
    lst.append(ele)
arr=np.array(lst)
print(type(arr))

print(sorted(arr))



