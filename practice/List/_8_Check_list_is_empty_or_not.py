lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")

if len(lst):
    print("----------*******---------------")
    print("list is not empty")
    print("--------------------------------")
else:

    print("----------*******---------------")
    print("list is empty")
    print("--------------------------------")