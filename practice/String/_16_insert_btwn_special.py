s="/*-+!@#*(&^$"
st=input("enter the string to insert")
i=int(input("enter the position where you need to enter"))

st3=""
for j in range(len(s)):
    if j!=i:
        st3=st3+s[j]
        print(st3)
    elif j==i:
        st3=st3+st

print(st3)

