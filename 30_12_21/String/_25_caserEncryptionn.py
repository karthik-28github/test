#program to create a Caesar encryption
class Demo:
    def __init__(self):
        pass
    def encry(self,a):
        b=""
        num=int(input("enter the secret number "))
        for i in a:
            j=ord(i)+num
            print(chr(j),end="")
            # b=" ".join(chr(j))
d=Demo()
a="karthik"

print("the given String is ",a)
b=d.encry(a)
print("the encrypted String is ",b)