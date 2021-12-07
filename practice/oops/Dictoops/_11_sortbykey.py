#Sort Counter by value.

class Demo:
    def __init__(self):
        self.temp=0
        self.b=dict
    def srt(self,dict1):
        b=dict(sorted(dict1.items(), key=lambda x: x[0]))
        print(b)


d=Demo()
a={4:"karthik",5:"sun",3:"moon",1:"star",2:"universe"}
d.srt(a)
