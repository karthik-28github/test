class Dictmerge:
    def dict_merge(self,dict1,dict2):
        # dict3=self.dict1+self.dict2
        dict1.update(dict2)
        print(dict1)

dict1={'a':1,'b':2,'c':3}
dict2={'d':4,'e':5,'f':6}
d1=Dictmerge()
d1.dict_merge(dict1,dict2)

