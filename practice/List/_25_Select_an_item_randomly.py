import random
lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print("Original list is : " + str(lst))
print("--------------------------------")

rand_idx = random.randint(0, len(lst) - 1)
random_num = lst[rand_idx]
print("--------------------------------")
print("--------------------------------")
print("Random selected number is : " + str(random_num))
print("--------------------------------")