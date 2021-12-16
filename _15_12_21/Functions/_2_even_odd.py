#Print even and odd using funtions

class Eo:
    def __init__(self):
        pass
    def even(self,a):
        for i in a:
            if i%2==0:
                print(i,end=" ")
    def odd(self,a):
        for i in a:
            if i%2!=0:
                print(i,end=" ")





e=Eo()
a=list(range(1,50))
print("even numbers are")
e.even(a)
print("\n")
print("odd numbers are")
e.odd(a)
