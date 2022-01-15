#count no of prime numbers less than the given number


n=int(input("enter a number "))


for i in range(n):
    lst = []
    if n == 1 or n == 2:
        lst.append(n)
    else:
        for i in range(3, n - 1):
            if n % i == 0:
                pass
            else:
                lst.append(i)
print(lst)