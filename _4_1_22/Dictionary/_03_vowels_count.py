#to count number of vowels in strings
class Vowelscount:
    list1 = ['a', 'e', 'i', 'o', 'u']

    def __init__(self,a):
        self.a_lower = a.lower()
        print(self.a_lower)
        pass

    def vowels(self):
        for i in Vowelscount.list1:             #for calling class variableneed to mention class name.
            for j in self.a_lower:
                pass
            print(f'occurances of \'{i}\' is: {self.a_lower.count(i)} times.')



a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''

v1=Vowelscount(a)
v1.vowels()
print("--------------------------------------------------")

#to count number of vowels in strings
class Vowelscount:
    list1 = ['a', 'e', 'i', 'o', 'u']

    def __init__(self,a):
        self.a_lower = a.lower()
        print(self.a_lower)
        pass

    def vowels(self):
        for i in Vowelscount.list1:             #for calling class variableneed to mention class name.
            for j in self.a_lower:
                pass
            print(f'occurances of \'{i}\' is: {self.a_lower.count(i)} times.')

a = input("Enter Text here :")

v1=Vowelscount(a)
v1.vowels()