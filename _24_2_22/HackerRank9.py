'''
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
'''

str1=input()

sl=[val for val in str1 if val.islower() ]
su=[val for val in str1 if val.isupper() ]
no=[val for val in str1 if val.isdigit() and int(val)%2!=0  ]
ne=[val for val in str1 if val.isdigit() and int(val)%2==0  ]

sl=sorted(sl,reverse=False)
su=sorted(su,reverse=False)

for i in sl:
    print(i,end="")
for i in su:
    print(i,end="")
for i in no:
    print(i,end="")
for i in ne:
    print(i,end="")