#in equal triangle
#The sum of 2sides should be greater than the 3rd side


flag=False
side=[]
while len(side)<=2:
    n=int(input("enter the side"))
    side.append(n)
print(side)

if side[0]+side[1]>side[2]:
    flag=True
else:
    flag=False
if side[1]+side[2]>side[0]:
    flag=True
else:
    flag=True
if side[2]+side[0]>side[1]:
    flag=True
else:
    flag=False

if flag:
    print("it is a equal triangle")
else:
    print("it is not  a equal triangle")

