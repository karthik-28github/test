#1295. Find Numbers with Even Number of Digits

list1=[]
n=int(input("enter how many elemts in the array"))
for i in range(n):
    ele=int(input("enter the element"))
    list1.append(ele)


even=[]
odd=[]
for j in range(len(list1)):
    if len(str(list1[j]))%2==0:
        even.append(list1[j])
    else:
        odd.append(list1[j])
print("the element which has even number of elemens are",even)
print("the element which has odd number of elemens are",odd)
