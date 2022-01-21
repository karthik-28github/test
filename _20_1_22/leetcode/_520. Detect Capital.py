#520. Detect Capital


str1=input("enter the string ")


for i in range(len(str1)):
    if i==len(str1):
        if str1[i].isupper():
            print("the word u have givin has last capital word")

    if i==1:
        if str1[i].isupper():
            print("the word u have givin has first capital word")