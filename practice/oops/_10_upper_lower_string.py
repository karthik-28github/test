class Strul:
    def __init__(self):
        pass
    def upper_lower(self,string1):
        print(f'text in upper case {string1.upper()}')
        print(f'text in lower case {string1.lower()}')

string1=input('Enter text here:')

s1=Strul()
s1.upper_lower(string1)