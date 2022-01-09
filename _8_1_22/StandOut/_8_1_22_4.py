#picking currency excahnges
coin=[1,2,5]
notes=[10,50,100,200,500,2000]


num=int(input("enter the amount"))
change=""
n=0

if num>=2000:
    n=num//2000
    print(n,2000)
    for i in range(n):
        change=change+str(2000)
        change=change+"+"
        num=num-2000
if num>=500:
    n = num // 500
    print(n, 500)
    for i in range(n):
        change = change + str(500)
        change =change+"+"
        num = num - 500
if num>=200:
    n = num // 200
    print(n, 200)
    for i in range(n):
        change = change + str(200)
        change =change+"+"
        num = num - 200
if num>=100:
    n = num // 100
    print(n, 100)
    for i in range(n):
        change = change + str(100)
        change =change+"+"
        num = num - 100
if num>=50:
    n = num // 50
    print(n, 50)
    for i in range(n):
        change = change + str(50)
        change =change+"+"
        num = num - 50
if num>=10:
    n = num // 10
    print(n, 10)
    for i in range(n):
        change = change + str(10)
        change =change+"+"
        num = num - 10
if num>=5:
    n = num // 5
    print(n, 5)
    for i in range(n):
        change = change + str(5)
        change =change+"+"
        num = num - 5
if num>=2:
    n = num // 2
    print(n, 2)
    for i in range(n):
        change = change + str(2)
        change =change+"+"
        num = num - 2
if num>=1:
    n = num // 1
    print(n, 1)
    for i in range(n):
        change = change + str(1)
        change =change+"+"
        num = num - 1
leng=change
print(change)