#476. Number Complement
#print the compliment of the number
#conver each 1 to 0 and each 0 to 1 so that you will get the compliment of a number
#first conver a number to its binary format


n=int(input("enter a number "))

str1=bin(n)
str2=str1[2:]
str3=""



print("the binary format of the givin number",n,"is ",str2)
for i in str2:
    if i=="1":
        str3=str3+"".join("0")
    else:
        str3=str3+"".join("1")
print("the 1's complement or the negation of the givin word is ",str3)
