#create dict using lists
class Demo:
    def __init__(self):
        pass
    def prnt_rpd(self,lst):
        dict1={}
        for i in range(len(lst)):
            dict1[i]=lst[i]
        print(dict1)


d=Demo()
lst=[10,10,20,20,30,30,40,40]
d.prnt_rpd(lst)