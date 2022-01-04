class Swapfl():
    def __init__(self):
        pass
    def swap_f_l(self,string1):
        start=string1[0]
        end=string1[-1]
        swapped_string=end+string1[1:-1]+start
        print(swapped_string)

# should implement removing special characters
user_input = input("Enter string here:")
s1=Swapfl()
s1.swap_f_l(user_input)
