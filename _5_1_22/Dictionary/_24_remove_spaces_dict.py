#Remove spaces from dictionary keys.

class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        for i in dict1:
            for j in  i:
                if j==" ":
                    dict1[i]
d=Demo()
shop={"so ap":1000,"s hampoo":200,"bisc uits":900,"toothbr ush":500,"mil k":150,"cig ate":650}
d.prnt(shop)