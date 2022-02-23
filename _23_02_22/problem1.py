#power and sum the list of numbers
lst1=list(map(int,(input().split())))

lst2=[]
dict1={}
for i in lst1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1

for i,j in dict1.items():
    print(list(map(int,(str(i)*j))))
sum=0
for i,j in dict1.items():
    sum+=pow(i,j)

print("the sum of values is",sum)

