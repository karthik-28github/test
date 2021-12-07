list1 = []
num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

print("--------------------------------")
print("----------*******---------------")
print("Smallest element is:", min(list1))
print("--------------------------------")
print("----------*******---------------")
list1.sort()
print("--------------------------------")
print("----------*******---------------")
print("Smallest element is:", *list1[:1])
print("--------------------------------")

