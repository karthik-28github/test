st=input("enter the string ")
i=int(input("enter position where you need to replace"))
st1=input("enter what you need to replace")


for j in range(len(st)):
    if j==i:
        print(st[i])

print(st)