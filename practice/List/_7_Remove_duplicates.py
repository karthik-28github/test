lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")
print("----------*******---------------")

temp_list = []

for i in lst:
    if i not in temp_list:
        temp_list.append(i)

lst = temp_list

print("List After removing duplicates ", lst)

print("--------------------------------")
print("----------*******---------------")
my_final_list = set(lst)
print("List After removing duplicates using set ",list(my_final_list))
print("--------------------------------")
