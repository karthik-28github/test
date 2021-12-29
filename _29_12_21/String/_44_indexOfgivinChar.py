#print the index of the character in a string
class Demo:
    def __init__(self):
        pass
    def chk(self,str1,ele):
        count=0
        for i in str1:
            count+=1
            if i==ele:
                print("the element",ele,"availble at the position",count)
                print(str1)


d=Demo()
str1="qwertyuiopasdfghjklzxcvbnm"
ele=input("enter an alphabet")
d.chk(str1,ele)
