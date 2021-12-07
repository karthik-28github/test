list1 = []
num = int(input("Enter number of elements in list1: "))
print("--------------------------------")
print("----------*******---------------")
for i in range(1, num + 1):
    print("--------------------------------")
    ele = int(input("Enter elements for list 1: "))
    list1.append(ele)
print("--------------------------------")
print("----------*******---------------")
print(list1)
def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Second Largest element is:", list1[length - 2])
print("----------*******---------------")
sec_Largest = find_len(list1)
print("----------*******---------------")