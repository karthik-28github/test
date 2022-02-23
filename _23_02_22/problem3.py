#reverse the words available in the sentence


str1=input("enter the string")
lst=[]
for i in str1.split():
    lst.append(i[::-1])
s2=" ".join(lst)
print(s2)