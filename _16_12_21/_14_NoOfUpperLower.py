class Demo:
    def __init__(self):
        self.lower=0
        self.upper=0
    def count(self,a):
        for i in a:
            if i.isupper():
                self.upper+=1
            if i.islower():
                self.lower+=1
        print("upper case is ",self.upper,"and lower case is ",self.lower)


d=Demo()
a="KaRtHik"
d.count(a)