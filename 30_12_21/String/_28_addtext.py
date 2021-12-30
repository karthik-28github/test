class Demo:
    def __init__(self):
        pass
    def pri(self,a):
        for i in a:
            print(i,end=" ")
            if i =="\n":
                print("***")

d=Demo()
a="""hai my name is karthik
    im from anekal 
    my highest qualification is bca
    i love programming"""
d.pri(a)
