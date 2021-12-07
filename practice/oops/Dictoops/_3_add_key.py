#Add a key

class Add_Key(dict):
    def _init_(self):
        self = dict()
    def final(self,key,value):
        self[key] = value
a = Add_Key()
a.final(1,'one')
a.final(2,'two')
a.final(6,'hyee')
print(a)