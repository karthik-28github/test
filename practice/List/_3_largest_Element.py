#largest element in a list
lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")
print("----------*******---------------")
lst.sort()
print("Largest element is from the list:", lst[-1])
print("----------*******---------------")
print("Largest element is:", max(lst))
print("----------*******---------------")
print("--------------------------------")


def myMax(lst):
    max = lst[0]
    for x in lst:
        if x > max:
            max = x

    return max
print("Largest element by using function is:", myMax(lst))
