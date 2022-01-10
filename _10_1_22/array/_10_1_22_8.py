#axis of array

import numpy as np

a=np.array([(1,2,3,4),(5,6,7,8)])

print(a.sum(axis=0))
print(a.sum(axis=1))


#square root
print(np.sqrt(a))

#standederd devitatiom
print(np.std(a))



#vertical and horizantal stacking

n1=np.array([(1,2,3),(4,5,6)])
n2=np.array([(1,2,3),(4,5,6)])

print(np.vstack((n1,n2)))
print(np.hstack((n1,n2)))

print(np.ravel((n1,n2)))