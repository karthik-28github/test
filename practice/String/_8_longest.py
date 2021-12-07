#length of longest string in python
st3 = input("Enter sentence : ")
lt3 = st3.split(" ")
max_length = 0
for i in lt3:
    if(max_length < len(i)):
        max_length = len(i)
print("Longest word length : ",max_length)