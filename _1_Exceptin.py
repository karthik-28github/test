#compute sum of digits of a given string
b=[]
sum=0
a=int(input("enter how many  number you want to enter  "))
for k in range(a):
    try:
        i=input("enter the numbers ")
        j=int(i)
        b.append(j)
        sum=sum+j
    except Exception as e:
        print(e)
print(b)
print("the sum of digits in string is ",sum)


