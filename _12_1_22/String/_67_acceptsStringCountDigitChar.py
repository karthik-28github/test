#that accepts a string and calculate the number of digits and letters
class Demo:
    def __init__(self):
        pass
    def calc(self,a):
        countd=0
        countc=0
        for i in a:
            if i.isdigit():
                countd+=1
            if i.isalpha():
                countc+=1
        print("the count of characters is",countc,"and the count of digits are",countd)


d=Demo()
a="Karthik280"
d.calc(a)