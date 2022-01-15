#capitalize the title
#if the word is less than 3 make everything as lower case
#if the word is more or equal to 3 letters then make all first char to captial and all others chars as lower case

str1 = 'geeKs foR geEks'
str2 = str1.title()
print('First Output after Title() method is = ', str2)

# observe the original string
print('Converted String is = ', str1.title())
print('Original String is = ', str1)

# Performing title() function directly
str3 = 'KArthiK kuMAr'.title()
print('Second Output after Title() method is = ', str3)

str4 = 'im in bangalore'.title()
print('Third Output after Title() method is = ', str4)

str5 = '6041'.title()
print('Fourth Output after Title() method is = ', str5)