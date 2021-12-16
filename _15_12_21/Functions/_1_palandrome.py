#check the givin word is palandrome or not
class Paladrome:
    def __init__(self):
        pass
    def pri(self,a):
        le=len(a)
        b=a[::-1]
        if a==b:
            pal=True
        else:
            pal=False

        print(a,b)
        if pal==True:
            print("the entered String is Palandrome")
        else:
            print("the entered String is not a Palandrome")




p=Paladrome()
a=input("enter the String")
p.pri(a)