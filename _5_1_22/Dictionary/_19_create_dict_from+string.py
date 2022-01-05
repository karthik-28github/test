#Create a dictionary from a string.

class Demo:
    def __init__(self):
        pass
    def prnt(self,dict1):
        dict2={}
        j=1
        for i in dict1.split(" "):
            dict2[j]=i
            j+=1
        print(dict2)
d=Demo()
str1="hello my name is karthik"
d.prnt(str1)

