#convert one dimentional array to two dimentional array


a=[]
print("the array elemets is ",a)
print("\n")

num=int(input("how many elemts you are willing to enter"))
for i in range(num):
    ele=int(input("enetr the elemets "))
    a.append(i)
print(a)



if  len(a)%2!=0:
    print("the elemet count is not even so cant make 2d array ")

col1=[]
col2=[]
if len(a)%2==0:
    for i in range(len(a)):
        if i==0 or i%2==0:
            col1.append(a[i])
        else:
            col2.append(a[i])
print(col1)
print(col2)