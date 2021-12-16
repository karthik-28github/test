#table of a givin number

class Demo:
    def __init__(self):
        pass
    def tab(self,a):
        for i in range(1,10):
            print(a,"*",i,"=",a*i)




d=Demo()
a=int(input("enter number to find the table of: "))
d.tab(a)