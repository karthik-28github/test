class Demo:
    def __init__(self):
        c=dict
    def merge(self,key,values):
        c=dict(zip(key,values))
        return c





d=Demo()
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary =d.merge(keys,values)
print(color_dictionary)