class Demo:
    def __init__(self):
        pass
    def typ(self,a):
        for i,j in a.items():
            print(type(j))







d=Demo()
a={1:10,2:4.5,3:"hai",4:"/",5:"0.0000000008"}
d.typ(a)