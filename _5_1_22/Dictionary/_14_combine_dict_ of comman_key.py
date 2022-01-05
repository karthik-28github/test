#Combine two dictionary adding values for common keys.


#Count number of items in a dictionary value that is a list


class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1,dict2):
        dict3={}
        dict3=(dict1,dict2)
        print(dict3)




d=Demo()
d1={1:10,2:20,3:30,4:40,5:50,6:60}
d2={1:1,2:2,3:3,4:4,5:5,6:6}
d.prnt(d1,d2)