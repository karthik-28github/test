#Combine values in python list of dictionaries.


class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1,dict2,dict3):
        dict4={}
        dict4.update(dict1)
        dict4.update(dict2)
        dict4.update(dict3)

        print(dict4)

d=Demo()
val1={1:["karthik",24,"anekal"]}
val2={2:["sachin",27,"bangalore"]}
val3={3:["abhi",25,"mandya"]}
d.prnt(val1,val2,val3)

