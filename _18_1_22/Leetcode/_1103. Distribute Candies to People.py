#candies and number of kids

candy=int(input("enter the value of candies"))
kids=int(input("enter the number of kids "))

lis=[0  for x in range(kids)]
for i in range(1,candy):
    for j in range(kids):
        lis[j]=i
        i+=1
print(lis)