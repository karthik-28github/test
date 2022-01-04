class Specifiedchar:
    def __init__(self):
        pass
    def startchar(self,string1,start_char):
        res=string1.startswith(start_char)
        print(res)

string1=input("Enter a text here:")
start_char=input("check char start with:")

s1=  Specifiedchar()
s1.startchar(string1,start_char)