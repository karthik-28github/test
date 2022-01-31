#945. Minimum Increment to Make Array Unique

arr=[3,2,1,2,1,7]

arr1=[]
for i,j in enumerate(arr):
    print(j)
    if j not in arr1:
        arr1.append(j)
    else:
        new=j
        while True:
            new+=1
            if new not in arr1:
                arr1.append(new)
                break

print(arr)
print(arr1)