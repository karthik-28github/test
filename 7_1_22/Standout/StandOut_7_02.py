#program to create a multi dimentional arrary

import array as arr



n=int(input("enter the number of rows"))
m=int(input("enter the number of colums"))

arr1=["i"]
for i in range(n):
    col=[]
    for j in range(m):
        col.append("*")
    arr1.append(col)
for i in arr1:
    print(i)
