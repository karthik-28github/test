class Counts:
    def __init__(self):
        pass
    def count_word(self,a):
        frequencies = collections.Counter(a)
        repeated = {}
        for key, value in frequencies.items():

            if value > 1:
                repeated[key] = value
            else:
                print(f'{key} is not repeating')
        print(repeated)


import collections
a=input("Enter string:")

c1=Counts()
c1.count_word(a)

