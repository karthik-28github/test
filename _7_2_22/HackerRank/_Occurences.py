'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Concept

Some string processing examples, such as these, might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function len(s), where  is the string.
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over  to .  is excluded.

Language
Pypy 3

More
12345678910111213141516171819
def count_substring(ip, op):
    count=0
    num=0
    while num < len(ip):
        a = ip.find(op)
        if a > 0:
            count += 1

        if ip.find(op, a, len(op) + 1):
            ip = ip.replace(op[0], "*", 1)
            num += 1

    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
Line: 19 Col: 17

Submit Code

Run Code

Upload Code as File

Test against custom input
Terminated due to timeout :(

Ask your friends for help:Share on FacebookShare on TwitterShare on LinkedIn

Test case 3

Test case 4

Test case 5

Test case 8

Test case 0

Test case 1

Test case 2

Test case 6

Test case 7

Test case 9
Compiler Message
Time limit exceeded
Your code did not execute within the time limits. Please optimize your code. For more information on execution time limits, refer to the environment page
Hidden Test Case
Unlock this testcase for 5 hackos.

Unlock
Contest Calendar
'''
def count_substring(ip, op):
    count = 0
    num = 0
    while num < len(ip):
        a = ip.find(op)
        if a > 0:
            count += 1

        if ip.find(op, a, len(op) + 1):
            ip = ip.replace(op[0], "*", 1)
            num += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)