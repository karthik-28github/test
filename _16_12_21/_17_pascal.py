class Function:
    def _init_(self):
        pass
    def factorial(n):
        fact=1
        for x in range(1,n+1):
            fact=fact*x
        return fact
    def pascal(self,n):
        for i in range(n):
            for k in range(n - i + 1):
                print(end="  ")
            for j in range(i + 1):
                # f(i)//(f(j)-f(i-j))
                print((Function.factorial(i) )// ((Function.factorial(j) * Function.factorial(i - j))), end="   ")
            print()
me=Function()

print(me.pascal(10))