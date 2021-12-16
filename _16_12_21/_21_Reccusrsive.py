
def facto(num):
    #false condition
    if num == 1:
        return num
    #recursion condition
    else:
        return num*facto(num-1)

a=lambda x:x*a(x-1)
num=5
print(facto(num))
print(a)

