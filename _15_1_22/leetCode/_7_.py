#
# import math
#
# a=2
# b=-2
# res=1
# if b>0:
#     for i in range(1,b+1):
#         res=res*a
#     print(res)
# else:
#     b =(-1)*(b)
#     # print(b)
#     for i in range(1,b+1):
#         d=res*a
#     res=1/d
#     print(res)
#happy number
num=int(input("enter the number"))

while num>10:
    res=0
    num1=str(num)
    for i in num1:
        res=res+int(i)*int(i)

    print(num1[0],"^2",'+',num1[1],"^2",'=',res)
    num=res
if num!=1:
    print("unhappy number")
else:
    print("happy number")

