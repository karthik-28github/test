#check whether the number is in givin range or not

class Demo:
    def __init__(self):
        pass
    def pri(self,a,b):
        if b in a:
            print(b,"is in range of",a)
        else:
            print(b, "is not in range of",a)



d=Demo()
a=range(1,10)
b=int(input("enter the number "))
d.pri(a,b)