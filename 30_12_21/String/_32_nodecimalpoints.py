#print the following floating numbers with no decimal places
class Demo:
    def __init__(self):
        pass
    def pri(self,a):
        for i in a:
            format_float="{:.0f}".format(i)
            print(format_float)




d=Demo()
a=[-2.54789,3.54782,9.46875,8.0314,-7.692,-4.9482]
d.pri(a)