class Replacedotcomma:
    def __init__(self):
        pass
    def Replace(self,a):
        a = a.replace(',','#')
        a = a.replace('.',',')
        a = a.replace('#','.')
        return a

a = input("enter text with comma and dot:")
r1=Replacedotcomma()
a_str=r1.Replace(a)
print(f'original text:{a}')
print(f'replaced dot and comma:{a_str}')