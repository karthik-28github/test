#961. N-Repeated Element in Size 2N Array
#give thee number which has been repeated more time


num=[5,1,5,2,5,3,5,4]
dict1={}

for i in num:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
dict2=max(dict1.items())
i,j=dict2
print(f"the number",i,"has been repeated ",j,"number of times")
