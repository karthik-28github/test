#count and display the vowels of a given text
vowels=['a','e','i','o','u']
str1="hello my name is karthik and im from anekal"
count=0

for i in str1:
    if i in vowels:
        count+=1
print("the total numbers of voowels in the givin string is ",count)
