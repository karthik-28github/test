#key alredu exists
class Key:
    def __init__(self,dict):
        self.dict = dict
    def check(self,dict,key):
        self.dict = dict
        self.key = key
        if key in dict:
            print("-" * 40)
            print("Key is present")
            print("-" * 40)
            print("value is =",dict[key])
            print("-" * 40)
        else:
            print("not present")
dict = {'a': 100, 'b':200, 'c':300, 'hii':'welcome', 'news':'rain'}
print("-"*40)
key = input("enter your key which you want to check:")
k = Key(dict)
k.check(dict,key)