#sum of elements using oops
class Demo:
    def __init__(self):
        self.total=0
    def sum(self,a,b,c):
        for i in a:
            self.total = self.total + i
        for i in b:
            self.total = self.total + i
        for i in c:
            self.total = self.total + i
        return self.total


d=Demo()
a=[]
a1=int(input("how many values for a "))
for i in range(0,a1):
    a2=int(input("enter the list values for a "))
    a.append(a2)

b=[]
b1=int(input("how many values for b "))
for i in range(0,b1):
    b2=int(input("enter the list values for b "))
    b.append(b2)
c=[]
c1=int(input("how many values for c "))
for i in range(0,c1):
    c2=int(input("enter the list values for c "))
    c.append(c2)
# b=list(int(input("enter the list values for b ")))
# c=list(int(input("enter the list values for c ")))

total=d.sum(a,b,c)
print(total)