#program to get dict key dict value and dict items

class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        for i,j in dict1.items():
            print("key :",i)
            print("value :",j)
            print("iteams",(i,j))

d=Demo()
dic={1:1000,2:200,3:900,4:500,5:150,6:650,7:100}
d.prnt(dic)