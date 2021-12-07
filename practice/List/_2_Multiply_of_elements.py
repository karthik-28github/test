#Mulitply of elements

lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")

print("-----------********---------------------")


def multiplyList(lst):
    # Multiply elements one by one
    result = 1
    for x in lst:
        result = result * x
    return result

totalmult = multiplyList(lst);
print('multiplication of elements using function: ', totalmult)
print("--------------------------------")
print("-----------********---------------------")

print("-----------********---------------------")