#483 Max Consecutive zeros


lst=[1,1,1,1,54,1,1,1,1,1,1,1,1,1,9,7,2,3,5,0,1]
count=0
consi=0
for i in lst:
    if i==0:
        count=count+1
    else:
        consi=max(consi,count)
        count=0

print("the maximum number of consective 0s is",consi)

