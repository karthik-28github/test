#796. Rotate String

str1="abcde"
str0=str1
str2="deabc"

count=0
while(str1!=str2):
    print(str1)
    str1=str1[1:]+str1[:1]
    count+=1

print("it took",count,"number of rotations to convert",str0,"to","str2")