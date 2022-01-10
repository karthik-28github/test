#reshape and slicing in the array
#charing rows to colums and colums to row is called as reshaping

import numpy as np

n=np.array([(1,2,3,4),(5,6,7,8)])
print(n)

n=n.reshape(4,2)
print(n)


n1=np.array([(1,2),(3,4),(5,6)])
print(n1)
n1=n1.reshape(2,3)
print(n1)
