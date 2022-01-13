string1 = input("Enter string:")
output = ''
for i in range(len(string1)):
    if string1[i] == '.':
        output = output + ','
    elif string1[i] == ',':
        output = output + '.'
    else:
        output = output + string1[i]
print(output)