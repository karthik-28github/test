#sort list alphabetically in a dictionary

class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        lst=dict1[1]
        dict1[1]=sorted(lst)
        print(dict1)
d=Demo()
dic={1:["g,f,e,z,q,t,y,b,k,l,p,x"]}
d.prnt(dic)