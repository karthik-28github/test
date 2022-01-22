#658. Find K Closest Elements
#enter the list
#enter a number and find the nearest or closest element


lst=[1,4,9,15,20,21,25,30,35,40]

n=int(input("enter the number "))
min1=[]
for i in lst:
    min1.append(i-n)

min2=min(min1)
print("the nearest number for ",n,"is ",n+min2)
