##move spaces to the front of a given string

str1="hel   lo"
str2=""
for i in str1:
    if i!=" ":
        str2+=" ".join(i)
print(str2)