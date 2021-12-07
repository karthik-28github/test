lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")

m= int(input("enter the element which you need to know the index :"))
print("--------------------------------")
print("---------**********---------------")
print("Index at which element ",m,"is present :", lst.index(m))
print("--------------------------------")