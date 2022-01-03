def odd(n):
    if n <= 1:
        return n
    elif n%2 != 0:
        print(n)
        return odd(n-2)

num = 9
if num%2==0:
    num=num-1
ans=odd(num)
print(ans)