string1="python is awesome,isn't it?"
substring="is"

class Occurances:
    def __init__(self):
        pass
    def occurance_substring(self,string1,substring):
        sub_string_count=string1.count(substring)
        print(sub_string_count)

string1=input("Enter string:")
substring=input("substring to find:")
s1=Occurances()
s1.occurance_substring(string1,substring)