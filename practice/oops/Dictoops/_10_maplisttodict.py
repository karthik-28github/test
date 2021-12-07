#Map two lists into a dictionary

class Demo:
    def __init__(self):
        pass
    def Dic(self,keys,values):
        color_dictionary = dict(zip(keys, values))
        print(color_dictionary)


d=Demo()
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
d.Dic(keys,values)
