#find the first repeated character of a given string where the index of first occurrence is smallest


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
        a=list(d)
        first=a[0]
        for i,j in d.items():
            if i==first:
                print(first,j)

d=Demo()
str1="hello my name is karthik ,how are you"
d.occ(str1)