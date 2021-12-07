class Demo:
    def __init__(self):
        self.dict1={}
    def count1(self,a):
        for i,j in a.items():
            count=len(j)
            self.dict1[i]=count
        print(self.dict1)



d=Demo()
a={1:[1,2,3,4,5,6],2:[1,2,3,4,5,6,7,8],3:[1,2,4,9,6,3,7,5,1,3,5,78]}
d.count1(a)