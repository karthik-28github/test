#check if a string contains all letters of the alphabet

class Demo:
    def __init__(self):
        pass
    def chck(self,str1):
        a=list(range(97,97+26))
        b=[]
        boo=False
        for i in a:
            b.append(chr(i))

        for i in b:
            if i not in str1.lower():
                boo=False
                break
            else:
                boo=True

        return boo



d=Demo()
b=input("enter the text")
c=d.chck(b)
if  c==False:
    print("not validd")
else:
    print("valid")