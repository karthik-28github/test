#Check multiple keys exists in a dictionary.


class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
       if len(dict1.keys())>2:
           print(True)


d=Demo()
dict_lst={"one":1,"two":2,"three":3,"four":4,"five":5}
d.prnt(dict_lst)