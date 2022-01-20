#403. Frog Jump
#a from can jump 1/2 step forword or backword


list1=[0,1,2,4,6,8,9,11,12,13]
lst=0
flag=False
for i in range(len(list1)-1):   
    print(list1[i],list1[i+1])
    if abs(list1[i+1]-list1[i])>2:
        flag=False
        break
    else:
        flag=True
if flag:
    print("the frog can reach the end")
else:
    print("the frog cant reach the end")

