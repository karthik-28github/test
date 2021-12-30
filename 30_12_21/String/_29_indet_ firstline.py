#to set the indentation of the first line
class Demo:
    def __init__(self):
        pass
    def prindent(self,a):
        print("\t",end="")
        for i in a:
            print(i,end="")
d=Demo()
a="""hai my name is karthik
    im from anekal 
    my highest qualification is bca
    i love programming"""
d.prindent(a)