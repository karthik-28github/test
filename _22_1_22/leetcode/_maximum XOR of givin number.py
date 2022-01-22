'''Given an array arr[] of size, N. Find the subarray with maximum XOR. A subarray is a contiguous part of the array.


Example 1:

Input:
N = 4
arr[] = {1,2,3,4}
Output: 7
Explanation:
The subarray {3,4} has maximum xor
value equal to 7.

Your Task:
You don't need to read input or print anything. Your task is to complete the function maxSubarrayXOR() which takes the array arr[], its size N as input parameters and returns the maximum xor of any subarray.
 '''


lst=[1,2,3,4]
lst1=[]
for i in lst:
    for j in lst:
        print(i^j,end=" ")
        lst1.append(i^j)
print("\n")
print("the max of XOR for",lst,"is ",max(lst1))