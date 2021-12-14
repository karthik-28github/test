#Counting number elementswithin a specified ranges


class Demo:
    def __init__(self):
        pass
    def pri(self,a):
        c=len(a)
        j=0
        b=int(input("enter the range"))
        for i in a:
            if j < b:
                print(i,end=" ")
                j=j+1



d=Demo()
a=[0,4,7,1,6,8,13,179,49,4,16,218,3189,217,117,329,127,67,31,94,5]
d.pri(a)