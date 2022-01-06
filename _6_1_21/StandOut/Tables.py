#table creation
def tab(n):
    x=1
    for i in range(1,n+1):
        if x<=n:
            if x==i:
                lst1=[f'{x}*{i}={i*x}'for i in range(1,10+1)]
                print(lst1)
                x+=1
num=int(input("enter  how many table you need from (1-n)"))
tab(num)