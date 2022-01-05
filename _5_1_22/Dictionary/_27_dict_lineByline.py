#Print dictionary line by line


class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        for i in dict1.items():
            print(i)


d=Demo()
dic={1:1000,2:200,3:900,4:500,5:150,6:650,7:100}
d.prnt(dic)