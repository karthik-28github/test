class Dictgen:
    def dict_gen(self,num):
        dict1={x: x*x for x in range(1, num)}
        print(dict1)
num=int(input("Enter number of values of dict:"))
d1=Dictgen()
d1.dict_gen(num)