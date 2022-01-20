#412. Fizz Buzz
#if i is divisible by 3 or 5 print fizz or buzz else print the value

n=int(input("enter the value of n"))
answer=["fizz","buzz"]
lst=[]
for i in range(1,n):
    if i%3==0:
        lst.append(answer[0])
    elif i%5==0:
        lst.append((answer[1]))
    else:
        lst.append(i)

print(lst)
