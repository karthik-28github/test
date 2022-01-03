def even(n):
    if n <= 1:
        return
    elif n%2==0:
        print(n)
        return even(n-2)

num = 11
if num%2!=0:
    num=num-1
ans=even(num)
print(ans)

