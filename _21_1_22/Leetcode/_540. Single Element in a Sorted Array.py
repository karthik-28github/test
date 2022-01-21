#540. Single Element in a Sorted Array

lst=[1,1,2,3,3,4,4,5,5]
dic={}

for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1


for i,j in dic.items():
    if j==1:
        print("the element",i,"is alone it has no repitation in ",lst)

