class Zero:
    def __init__(self):
        pass
    def zero(self,a):
        b=[]
        for  i in a.split("."):
            b.append(int(i))
        c=""
        for j in b:
            c=c+"."+str(j)
        print(c)


str1="0000192.0000158.0001000.00038000"
z=Zero()
z.zero(str1)