#letter combination of a phone number

import itertools
def combi(leng,*args):
    lst2=[]
    for i in args:
        for j in i:
            for k in j:
                lst2.append(k)
    print(lst2)
    perm=itertools.combinations(lst2,leng)
    lst3=[]
    for z in perm:
        str2=""
        for y in z:
            str2=str2+y
        lst3.append(str2)
    print(lst3)
    print("----------------------------end--------------------------")

print("-------------------------start--------------------------------")
number={1:[" "],2:["a","b","c"],3:["d","e","f"]
        ,4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],
        7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}

num=int(input("enter the digits"))
str1=str(num)
leng=len(str1)
print(type(str1))
lst=[]
for i in str1:
    lst.append(number[int(i)])
print(lst)
print("-------")
combi(leng,lst)

# l=itertools.combinations((lst[i]),2)

