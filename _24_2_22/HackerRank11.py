'''
any()
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.

Code

# >>> any([1>0,1==0,1<0])
# True
# >>> any([1<0,2<1,3<2])
False
all()
This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.

Code

# >>> all(['a'<'b','b'<'c'])
# True
# >>> all(['a'<'b','c'<'b'])
False
Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format

The first line contains an integer .  is the total number of integers in the list.
The second line contains the space separated list of  integers.

Constraints


Output Format

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

Sample Input

5
12 9 61 5 14
Sample Output

True

Explanation

Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer.

Hence, the output is True.

Can you solve this challenge in 3 lines of code or less?
There is no penalty for solutions that are correct but have more than 3 lines.

Language
Python 3

More
45678910111213141516171819202122
        print("False")
else:
    print("False")
Line: 22 Col: 19

Submit Code

Run Code

Upload Code as File

Test against custom input
Python
You have earned 20.00 points!
63/115 challenges solved.
55%
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn
Next Challenge

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4

Test case 5
Compiler Message
Success
Input (stdin)

Download
5
12 9 61 5 14
Expected Output

Download
True
Contest CalendarBlogScoring
'''
def isPositive(i):
    if i > 0:
        return True
    return False

def isPalindrome(i):
    if int(str(i)[::-1]) is i:
        return True
    return False

N = int(input())
storage = map(int, input().split())
storage = sorted(storage)

if all([isPositive(i) for i in storage]):
    if any([isPalindrome(i) for i in storage]):
        print("True")
    else:
        print("False")
else:
    print("False")
