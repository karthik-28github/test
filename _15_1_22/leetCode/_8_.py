"""
263. Ugly Number
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.
Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""
#ugly number
n=6
lst1=[2,3,5]
lst2=[]
for i in range(2,n):
    if n%i==0:
        lst2.append((i))
for i2 in lst2:
    if i2 not in lst1:
        a="false"
        break
else:
    a="true"
print(a)

