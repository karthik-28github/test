

from random import shuffle
lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")
print("----------*******---------------")
shuffle(lst)
print("After suffle list is :",lst)