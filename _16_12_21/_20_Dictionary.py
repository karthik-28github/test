#to match item in two Dictionary

class Demo:
    def __init__(self):
        pass
    def Chck(self,a,b):
        if  a.items()==b.items():
            print("it is same")
        else:
            print("it is not same")




d=Demo()
a={1:"karthik",2:"is",3:"good",4:"boy"}
b={1:"karthik",2:"is",3:"good",4:"boy"}
d.Chck(a,b)