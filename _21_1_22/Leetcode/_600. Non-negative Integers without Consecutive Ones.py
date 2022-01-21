#600. Non-negative Integers without Consecutive Ones
#just print the binary representation of a number which does not have a consecutive 1

n=int(input("enter the value "))
lst=[ele for ele in range(n+1)]
str1=[]
str3=[]
for i in lst:
    str2=bin(i)
    str1.append(str2[2:])

print(str1)
for j in str1:
    if "11" in j:
        pass
    else:
        str3.append(j)



print("the binary reprasentation of a range of number which dont have consecutive 1s",str3)


