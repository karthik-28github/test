#create a tuple with different data types

class Demo:
    def __init__(self):
        pass
    def create(self,y):
        c=tuple(y)
        print(type(c))
        print(c)




d=Demo()
y=[28,"karthik",91.16]
d.create(y)