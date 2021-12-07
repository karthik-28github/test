st=input("enter the string ")
st1=" "
i=1
for i in range(len(st)):
    if i%2==0:
        st1=st1+st[i]

print(st1)
