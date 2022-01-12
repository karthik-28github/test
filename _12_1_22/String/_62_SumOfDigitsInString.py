#compute sum of digits of a given string
class Demo:
    def __init__(self):
        pass
    def calc(self,a):
        countd=0
        for i in a:
            if i.isdigit():
                countd+=int(i)
        print(" the count of digits are",countd)


d=Demo()
a="Karthik280"
d.calc(a)