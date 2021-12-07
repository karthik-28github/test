#check whether the list is empty or not

class Demo:
    def __init__(self):
        pass
    def check(self,a):
        if len(a)==0:
            print("the is empty")
        else:
            print("the list is not empty")
            print("the list contians ",a)




d=Demo()
a=[]
d.check(a)