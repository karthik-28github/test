#remove duplicate characters of a given string

class Demo:
    def __init__(self):
        pass
    def remdup(self,a):
        b=set(a)
        c=""
        for i in b:
            c+=i
        print(c)
d=Demo()
a="karthik"
d.remdup(a)