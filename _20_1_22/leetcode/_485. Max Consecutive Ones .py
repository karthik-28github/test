#485. Max Consecutive Ones
#maximun number of 1's consecutilvy


lst=[1,1,1,1,54,1,1,1,1,1,1,1,1,1,9,7,2,3,5,1]
count=0
consi=0
for i in lst:
    if i==1:
        count=count+1
    else:
        consi=max(consi,count)
        count=0

print("the maximum number of consective 1s is",consi)