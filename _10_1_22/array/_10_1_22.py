#program to sum two matrix

import array as arr


n=int(input("enter number of rows"))
m=int(input("enter number of colums"))

arr1=[]
col1=[]
for i in range(n):
    for j in range(m):
        z=int(input("enter the elements"))
        col1.append(z)
arr1.append(col1)
for i in arr1:
    print(i)

