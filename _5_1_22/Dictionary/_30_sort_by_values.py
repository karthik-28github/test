#sort conter by values

class Demo:
    def __init__(self):
        pass
    def sort1(self,lst):
        print(sorted(lst.items(),key=lambda x:x[1]))

d=Demo()
dic={1:1000,2:200,3:900,4:500,5:150,6:650,7:100}
d.sort1(dic)