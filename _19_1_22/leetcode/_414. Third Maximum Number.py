#414. Third Maximum Number
#print the third max number in the givin list


list1=[1,2,3,90,5,6,7,8,9]

fh=sh=th=list[0]

for i in list1:
    print(i)
    if i>fh:
        th=sh
        sh=fh
        fh=max(i,fh)
    elif i>sh:
        th=sh
        sh=i
    else:
        th=i

print("the third highest number in the givin list is ",th)