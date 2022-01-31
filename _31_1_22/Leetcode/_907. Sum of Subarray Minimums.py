#907. Sum of Subarray Minimums
import itertools

lst=[3,1,2,4]
new=[]
for n in range(1,len(lst)+1):
    for i in itertools.combinations(lst,n):
        new.append(i)
result=0
print(new)
for j in new:
    for k in j:
        min1=min(j)
    result+=min1
print(result)