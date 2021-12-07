class Capital:
    def __init__(self):
        pass
    def cap_f_l(self,a):
        a1=a[0].capitalize()+a[1:-1]+a[-1].capitalize()
        print(a1)

a='green'
p1=Capital()
p1.cap_f_l(a)
print("-----------------------------")

class Capital:
    def __init__(self,a):
        self.string1=a

    def cap_f_l(self):
        a1=self.string1[0].capitalize()+self.string1[1:-1]+self.string1[-1].capitalize()
        print(a1)

a='green'
p1=Capital(a)
p1.cap_f_l()
print("-----------------------------")

class Capital:
    def __init__(self,a):
        self.string1=a

    def cap_f_l(self):
        a1=self.string1[0].capitalize()+self.string1[1:-1]+self.string1[-1].capitalize()
        print(f'capitalised first & last string: {a1}')

a=input("enter string:")
if a[0].isalpha() and a[-1].isalpha():
    p1=Capital(a)
    p1.cap_f_l()
else:
    print('enter strings only!')