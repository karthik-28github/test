#length of string using dictionary


class Demo:
    def __init__(self):
        leng=0
    def Length(self,a):
        for i in a:
            self.leng=len(a[i])
        print("the length of String in dict is",self.leng)


d=Demo()
a={1:"karthik"}
d.Length(a)
