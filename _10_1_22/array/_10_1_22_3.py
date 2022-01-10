#from to find the difference between list and numpy

import numpy as np
import time

size=10

list1=range(size)
list2=range(size)

start1=time.time()

result=[(x+y) for x,y in zip(list1,list2)]
print(result)
print((time.time()-start1)*100000000)


np1=np.arange(size)
np2=np.arange(size)

start2=time.time()
result1=np1+np2
print(result1)
print((time.time()-start2)*100000000)


