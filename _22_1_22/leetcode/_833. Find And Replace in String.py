#833. Find And Replace in String

str1="abcd"
str2=["eeee","ffff"]

if "a" in str1:
    str1=str1.replace("a",str2[0])
if "cd" in str1:
    str1=str1.replace("cd",str2[1])

print(str1)