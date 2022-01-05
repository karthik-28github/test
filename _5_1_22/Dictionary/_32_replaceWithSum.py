#replace values with their corresponding sum
class Demo:
    def __init__(self):
        pass
    def rep_sum(self,dict1):
        sum=0
        for i,j in dict1.items():
            sum+=j
            dict1[i]=sum
        return dict1


d=Demo()
d1={1:5,2:5,3:5,4:5,5:5}
print(d.rep_sum(d1))