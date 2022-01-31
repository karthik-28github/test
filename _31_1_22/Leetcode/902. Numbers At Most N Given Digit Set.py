#902. Numbers At Most N Given Digit Set
#first 4 numbers are 1 3 5 7
'''
Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.



Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
'''


n=int(input("enter the value of n"))
count=1
for i in range(n*10):
    if i%2==1:
        if "9" not in str(i):
            if count<=n:
                print(i)
                print("===",count)
                count+=1
