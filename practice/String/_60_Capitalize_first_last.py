string = input("Enter string:")
print("Entered string is:\'{}\'".format(string))

output_list = []
list_words = string.split(' ')
for word in list_words:
    output_list.append(word.capitalize())
print(output_list)

