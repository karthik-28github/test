#492. Construct the Rectangle
#all the possible way of creating a rectangle

val=int(input("enter the value"))
lst=[]
for i in range(1,val):
    if val%i==0:
        res=val//i
        print(res)
        lst.append([i,res])
        lst.append([res,i])

print(lst)