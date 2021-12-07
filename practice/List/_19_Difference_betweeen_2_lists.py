list1 = []
list2 = []
num = int(input("Enter number of elements in list1: "))
print("--------------------------------")
print("----------*******---------------")
for i in range(1, num + 1):
    print("--------------------------------")
    ele = int(input("Enter elements for list 2: "))
    list1.append(ele)
print("--------------------------------")
print("----------*******---------------")
print(list1)
print("--------------------------------")
print("--------------------------------")
num = int(input("Enter number of elements in list2: "))

for i in range(1, num + 1):
    print("--------------------------------")
    ele = int(input("Enter elements for list2: "))
    list2.append(ele)
print("--------------------------------")
print("----------*******---------------")
print(list2)
print("--------------------------------")


def Diff(list1, list2):
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))

print("Diffrence items between two list:",Diff(list1, list2))