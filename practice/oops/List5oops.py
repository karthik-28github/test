#Remove specified index from list and print


class Demo:
    def __init__(self):
        self.j=0
    def remove(self,a):
        i=int(input("enter the index to remove element from list "))
        print(a[i],"has been removed ")
        del a[i]
        print("the list after removing",a)


d=Demo()

a=[]
a1=int(input("how many values for a "))
for i in range(0,a1):
    a2=int(input("enter the list values for a "))
    a.append(a2)
b=input("do u want to remove the element from list  y/n")
if b=="y":
    d.remove(a)
