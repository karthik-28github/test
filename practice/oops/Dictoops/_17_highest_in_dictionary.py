# Python program to demonstrate
# finding 3 highest values in a Dictionary
class Asendingdesending:
    def __init__(self):
        pass
    def asd_des(self,dict1):
        print(f'3 Largest values in dicts are:{dict(sorted(dict1.items(), key = lambda x: x[1], reverse = True)[:3])}')

dict1={'a':2,'b':5,'c':7,'d':3,'e':4,'f':8,'g':1}
d1=Asendingdesending()
d1.asd_des(dict1)