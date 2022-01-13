#lowercase first n characters in a string

class Demo:
    def __init__(self):
        pass
    def pri(self,str1,n):
        j= len(str1)
        str2=""
        for i in range(n):
            str2=str2+str1[i].lower()
        str2=str2[:n]+str1[n:]
        print(str2)




d=Demo()
str1="KARTHIKKSHATRIYA"
n=int(input("enter how many char shld be in lower"))

d.pri(str1,n)
