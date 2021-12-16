#febanocii
class Demo:
    def __init__(self):
        self.feb=0
        self.f=0
        self.s=1
        self.t=0
    def pri(self,a):
        print(self.f)
        print(self.s)
        for i in range(2,a):
            self.t=self.f+self.s
            print(self.t)
            self.f=self.s
            self.s=self.t




d=Demo()
b=int(input("enter the number to find febanocii"))
d.pri(b)