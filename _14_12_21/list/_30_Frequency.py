#Get the frequency of the elements

class Demo:
    def __init__(self):
        pass
    def pri(self,a):
        d=dict()

        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        print(d)




d=Demo()
a=[1,2,3,4,7,6,8,9,1,4,5,9,3,0,0,4]
d.pri(a)