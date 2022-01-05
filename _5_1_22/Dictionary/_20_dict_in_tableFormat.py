#Print a dictionary in table format.

class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        for i,j in dict1.items():
            name,age,place=j
            print(f'{name}\t{age}\t{place}')

d=Demo()
val={1:["karthik",24,"anekal"],2:["sachin",27,"bangalore"],3:["abhi",25,"mandya"]}
d.prnt(val)

