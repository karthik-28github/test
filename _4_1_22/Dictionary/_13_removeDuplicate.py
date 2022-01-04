#



class Demo:
    def __init__(self):
        pass
    def duplicate(self,d):
        print(sorted(d.items()))
        dic=set(d.values())
        print(sorted(dic))

d=Demo()
dic={10:"k",5:"a",7:"l",9:"y",4:"x",3:"q",8:"d",6:"z",1:"r",2:"g",15:"g",99:"k"}
d.duplicate(dic)