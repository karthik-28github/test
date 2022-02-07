#tuple problem
'''
Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of .

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
Language
Pypy 3

More
12345
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))
Line: 5 Col: 19

Submit Code

Run Code

Upload Code as File

Test against custom input
Python
You have earned 10.00 points!
You are now 95 points away from the 4th star for your python badge.
14%125/220
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn
Next Challenge

Test case 0

Test case 1
Compiler Message
Success
Input (stdin)

Download
2
1 2
Expected Output

Download
3713081631934410656
Contest CalendarBlogScoring
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))