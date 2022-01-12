
name = input("Enter String")
count=0
count1=0

for i in name:
    if i.isdigit():
        count +=1
    elif i.isalpha():
        count1 += 1
    else:
        pass
print("the no of chars is",count1,"and the number of digits is",count)

