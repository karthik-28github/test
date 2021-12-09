a=[]
b=int(input("how many values"))

for i in range(b):
    j=int(input("enter the value"))
    a.append(i)


try:
    c=int(input("enter index to check the value"))
    for i in a:
        print(len(a))
        print(a[c])
except Exception as e:
    print(e)
