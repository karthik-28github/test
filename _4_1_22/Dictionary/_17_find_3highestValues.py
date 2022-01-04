#Find the highest 3 values in a dictionary.


class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        dict2=sorted(dict1.values())
        print(dict2[-3:len(dict1)])



d=Demo()
shop={"soap":1000,"shampoo":200,"biscuits":900,"toothbrush":500,"milk":150,"cigate":650}
d.prnt(shop)