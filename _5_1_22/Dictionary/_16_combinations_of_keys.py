#Create and display all combinations of letters, selecting each letter from a different key in a dictionary

import itertools

class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        lst=[]
        lst=dict1.keys()
        print(lst)
        per=itertools.permutations(lst)
        for i in per:
            print(i)


d=Demo()
shop={"soap":1000,"shampo":200,"biscuits":900,}
d.prnt(shop)