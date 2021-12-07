# print("-----USER INPUT CREATING THE LIST---------------")
# list1 = []
# list2 = []
# num = int(input("Enter number of elements in list1: "))
# print("--------------------------------")
# print("----------*******---------------")
# for i in range(1, num + 1):
#     print("--------------------------------")
#     ele = int(input("Enter elements for list 2: "))
#     list1.append(ele)
# print("--------------------------------")
# print("----------*******---------------")
# print(list1)
# print("--------------------------------")
# print("--------------------------------")
# num = int(input("Enter number of elements in list2: "))
#
# for i in range(1, num + 1):
#     print("--------------------------------")
#     ele = int(input("Enter elements for list2: "))
#     list2.append(ele)
# print("--------------------------------")
# print("----------*******---------------")
# print(list2)
# print("--------------------------------")
list1 = [6, 52, 74, 62]
list2 = [85, 17, 81, 92]

list2.extend(list1)
print("----------APPEND TO LIST2----------------------")
print("----------*******---------------")
print("After append to list2 new list2 is :",L2)
print("--------------------------------")

print("---FOR LIST1 COMMENT list2.extend(list1)  -------------")

print("--------------------------------")
list1.extend(list2)
print("-----------APPEND TO LIST1---------------------")
print("----------*******---------------")
print("After append to list1 new list1 is :",L1)
print("--------------------------------")