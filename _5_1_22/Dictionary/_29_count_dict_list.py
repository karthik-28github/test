#Count number of items in a dictionary value that is a list


class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        leng=0
        for i in dict1.values():
            leng=len(i)
        print("the length of the list in the dict is :",leng)




d=Demo()
dict_lst={1:[10,20,30,40,50,60,70,80,90,100,110]}
d.prnt(dict_lst)