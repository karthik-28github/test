#Get the maximum and minimum value in a dictionary.


class Demo:
    def __init__(self):
        pass
    def max_min(self,d):
        print("the maximun value in the dictionay is",max(d.values()))
        print("the maximun value in the dictionay is",min(d.values()))


d=Demo()
dic={10:"k",5:"a",7:"l",9:"y",4:"x",3:"q",8:"d",6:"z",1:"r",2:"g"}
d.max_min(dic)