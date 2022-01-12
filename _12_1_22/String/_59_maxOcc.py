# find the maximum occurring character in a given string

class Demo:
    def __init__(self):
        pass
    def occ(self,str1):
        d={}
        for i in str1:
            if(i!=' '):
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        a=max(list(d.values()))
        for j,k in d.items():
            if k==a:
                print(j,a)


d=Demo()
str1="hello my name is karthik ,how are you"
d.occ(str1)