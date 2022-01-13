#find the first non-repeating character in given string


class Demo:
    def __init__(self):
        pass
    def occ(self,str1):
        d={}
        for i in str1:
            if(i!=' ' and i!=','):
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        print(d)
        print("----")
        a=list(d)
        print(a)
        for i,j in d.items():
            if j==1:
                print(i,j)


d=Demo()
str1="hello my name is karthik ,how are you"
d.occ(str1)