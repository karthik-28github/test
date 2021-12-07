st=input("enter the string ")
i=int(input("enter the index"))
st1=""

for j in range(len(st)):
    if j==i:
        st1=st[j]
print(st1[0])