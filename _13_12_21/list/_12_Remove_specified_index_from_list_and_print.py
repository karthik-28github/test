lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)

print("-----------********---------------------")
print("-----------********---------------------")
print("after removing new list was ",lst)
print("-----------********---------------------")
print("-----------********---------------------")


def remove(lst, pos):
    del lst[pos]
    print(*lst)

pos = int(input("Enter the index where you want to delete : "))
remove(lst, pos)
print("-----------********---------------------")
print("list was: ",lst)
print("-----------********---------------------")



