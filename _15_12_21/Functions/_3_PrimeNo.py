#print prime numbers

class Prime:
    def __init__(self):
        self.pri=False
        self.b=[]
    def prim(self,a):
        for j in range(2,a):
            if a%j ==0:
                self.pri=False
                break
            else:
                self.pri=True
        if self.pri:
            print("prime")
        else:
            print("not prime")
p=Prime()

a=int(input("enter the number"))
p.prim(a)



