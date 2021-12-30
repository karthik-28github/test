'''Group Anagrams
Given an array of strings strs, group the anagrams together.You can return the answer in anyorder.
An Anagram is a word or phrase formed by rearranging theletters of a
different word or phrase, typically using all the original letters exactly once.

Example
1:

Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
Example
2:

Input: strs = [""]
Output: [[""]]
Example
3:

Input: strs = ["a"]
Output: [["a"]]
'''

lst1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
# lst1=[""]
# lst1=["a"]
print(f'original list is :{lst1}')

dict1={}
for i in lst1:
    i1="".join(sorted(i,reverse=False))
    dict1[i]=i1

d = {}
for key, value in dict1.items():
    if value not in d:
        d[value] = []
    d[value].append(key)

list1=list(d.values())
print(list1)