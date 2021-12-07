#Print all unique values in a dictionary.


class Demo:
    def __init__(self):
        pass
    def uniq(self,a):
        b=set(a.values())
        print(b)



d=Demo()
a={1: 'karthik', 2: 'chandra', 3: 'sachin', 4: 'hello', 5: 'sun', 6: 'world',7:"world"}

d.uniq(a)