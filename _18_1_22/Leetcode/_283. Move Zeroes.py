#if you have any 0 in the begining or in the middle of the array move that to the end of the array

import numpy as np

a=np.array([1,2,0,5,0,50,0,15,20,0])
b=np.array([])
c=np.array([])
d=np.array([])
for i in range(len(a)):
    if a[i]==0:
        c=np.append(c,a[i])
    else:
        b=np.append(b,a[i])
for j in range(len(b)):
    d=np.append(d,b[j])
for j in range(len(c)):
    d=np.append(d,c[j])

print(a)
print(b)
print(c)
print(d)
