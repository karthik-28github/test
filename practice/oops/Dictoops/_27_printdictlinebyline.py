class Demo:
    def __init__(self):
        pass
    def print1(self,a):
        for i,j in a.items():
            print(i)
            print(j)



d=Demo()
a={"A":{1:"one",2:"two",3:"three"},"B":{1:"one",2:"two",3:"three"}}
d.print1(a)