#different functions on array
#numpy

import numpy as np

arr1=np.array([1,2,3])


#gives the dimention of the array
print(arr1.ndim)

arr2= np.array([(1,2,3),(4,5,6)])
print(arr2.ndim)


#bytype size of array
print(arr1.itemsize)


#data type of the array
print(arr1.dtype)


#to know the size or len of array
print(arr1.size)


#to know the shape

print(arr2.shape)

