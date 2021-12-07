class Demo:
    def __init__(self):
        self.dict={}
    def evalu(self,a):
        self.dict = eval(a)
        print(self.dict['A'])
        print(self.dict['C'])






d=Demo()
string1 = "{'A':13, 'B':14, 'C':15}"

dict1=d.evalu(string1)


