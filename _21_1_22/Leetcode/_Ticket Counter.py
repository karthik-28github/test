#Ticket counter problem


n=int(input("enter the number of people standing"))
m=int(input("enter the ticket count for one time"))
lst=[ele for ele in range(1,n+1)]
flag=False
print(lst)
m1=m2=m
while len(lst)!=0:
    if flag==False:
        s1=0
        for i in lst[s1:m1]:
            print(i)
            val=lst[i]
        s1=m1
        m1=m1+m
        print("--",s1,m1)
        flag=True
    else:
        s2=-1
        for i in lst[s2:s2-3]:
            print(i)
            val=lst[i]
            s2=s2-3
        flag=False
