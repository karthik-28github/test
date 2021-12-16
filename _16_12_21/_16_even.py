#print the even numbers from a given list


class Eo:
    def __init__(self):
        pass
    def even(self,a):
        for i in a:
            if i%2==0:
                print(i,end=" ")




e=Eo()
a=list(range(1,50))
print("even numbers are")
e.even(a)