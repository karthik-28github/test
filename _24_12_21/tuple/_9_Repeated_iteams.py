# find the repeated items of a tuple

class Demo:
    def __init__(self):
        pass
    def create(self):
        b=[]
        a=int(input("how many valyes you are willing to enter"))
        for i in range(a):
            z=int(input("enter elements"))
            b.append(z)
        c=tuple(b)
        print(type(c))
        print(c)
        dict1=dict()
        for i in c:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]=dict1[i]+1
        print(dict1)
        for i,j in dict1.items():
            if j>1:
                print(i,"got repeated ",j,"times")




d=Demo()
d.create()