#table creation
def tab(n,m):
    if m==1:
        print(n,"*",m,"=",n*m)
    if m==2:
        print(n,"*",m,"=",n*m)
    if m==3:
        print(n,"*",m,"=",n*m)
    if m==4:
        print(n,"*",m,"=",n*m)
    if m==5:
        print(n,"*",m,"=",n*m)
    if m==6:
        print(n,"*",m,"=",n*m)
    if m==7:
        print(n,"*",m,"=",n*m)
    if m==8:
        print(n,"*",m,"=",n*m)
    if m==9:
        print(n,"*",m,"=",n*m)
    if m==10:
        print(n,"*",m,"=",n*m)
    else:
        for i in range(1,m+1):
            print(tab(n,i))





num=int(input("enter the number"))
for i in range(1,num+1):
    print(tab(i,10))