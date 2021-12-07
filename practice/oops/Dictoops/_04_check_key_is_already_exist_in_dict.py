class Dictkeyfind:
    def __init__(self,dict1):
        self.dict1=dict1
    def key_find(self,fkey1):
        if fkey1 in dict1:
            print(f'key {fkey1} is present in dict {dict1}')
        else:
            print(f'key {fkey1} is not present in dict {dict1}')

dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
fkey1='j'
d1=Dictkeyfind(dict1)
d1.key_find(fkey1)