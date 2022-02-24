'''
Given the time in numerals we may convert it into words, as shown below:

At , use o' clock. For , use past, and for  use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

Function Description

Complete the timeInWords function in the editor below.

timeInWords has the following parameter(s):

int h: the hour of the day
int m: the minutes after the hour
Returns

string: a time string as described
Input Format

The first line contains , the hours portion The second line contains , the minutes portion

Constraints

Sample Input 0

5
47
Sample Output 0

thirteen minutes to six
Sample Input 1

3
00
Sample Output 1

three o' clock
Sample Input 2

7
15
Sample Output 2

quarter past seven
'''
dict1={00:"o'",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
      11:"eleven",12:"twelve",13:"therteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",
      18:"eighteen",19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",
      24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine",30:"thirty"}

h=int(input())
m=int(input())

if m==00:
    print(f"{dict1[h]} {dict1[00]} clock")
if m==1:
    print(f"one minute past {dict1[h]} ")
if m>1 and m<15:
    print(f"{dict1[m]} minutes past {dict1[h]}")
if m==15:
    print(f"quarter past {dict1[h]}")
if m>15 and m<30:
    print(f"{dict1[m]} minutes past {dict1[h]}")
if m==30:
    print(f"half past {dict1[h]}")
if m>30 and m<45:
    print(f"{dict1[60-m]} minutes to {dict1[h+1]}")
if m==45:
    print(f"quarter to {dict1[h+1]}")
if m>45 and m<=59:
    print(f"{dict1[60-m]} minutes to {dict1[h+1]}")


