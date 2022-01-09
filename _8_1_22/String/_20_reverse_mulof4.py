# reverses a string if it's length is a multiple of 4


str1=input("enter the String")
a=len(str1)
print(a)
str2=" "
b=[ele for ele in range(100) if ele%4==0]
for i in b:
    if a==i:
        print(str1[::-1])



