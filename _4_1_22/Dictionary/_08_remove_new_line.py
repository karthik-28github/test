class Newlineremove:
    def __init__(self):
        pass
    def Remove_space(self,string):
        return " ".join(string.split())

string = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''

s1=Newlineremove()

String_without_space=s1.Remove_space(string)
print(String_without_space)

