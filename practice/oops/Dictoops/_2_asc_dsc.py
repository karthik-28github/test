#ascending and decending  order
import operator
class Ascen_Desen:
    def __init__(self,dict):
        self.dict = dict
    def value(self):
        ascen = dict(sorted(d.items(),key=operator.itemgetter(1)))
        print("-"*30)
        print("Ascending order will be:\n",ascen)
        print("-" * 30)
        desen = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        print("-" * 30)
        print("Descending order will be:\n",desen)
        print("-" * 30)
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a = Ascen_Desen(dict)
a.value()