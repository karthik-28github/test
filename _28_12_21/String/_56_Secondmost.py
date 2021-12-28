#find the second most repeated word in a given string


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
        a=(list(d.values()))
        b=set(a)
        a=list(b)
        for j,k in d.items():
            if k==a[-2]:
                print(j,k)

d=Demo()
str1="hello my name is karthik ,how are you"
d.occ(str1)
