import random
st=input("enter the string")

st1=list(st)
print(st1)
print(random.shuffle(st1))
st3="".join(st1)
print(st3)
