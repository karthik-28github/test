#print group of Strings

class Demo:
    def __init__(self):
        pass
    def grp(self):
        string1=""
        a=int(input("how many strings you meed to enter "))
        for i in range(a):
            str=input("enter the String ")
            string1=string1+str
        print(string1)

d=Demo()
d.grp()