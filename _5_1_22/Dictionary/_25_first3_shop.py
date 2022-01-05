#Get the top three items in a shop.

class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        j=1
        for i in dict1.items():
            if j<=3:
                print(i)
                j+=1
d=Demo()
shop={"soap":1000,"shampoo":200,"biscuits":900,"toothbrush":500,"milk":150,"cigate":650}
d.prnt(shop)