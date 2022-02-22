'''
collections.deque()
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

Click on the link to learn more about deque() methods.
Click on the link to learn more about various approaches to working with deques: Deque Recipes.

Example

Code
#
#>>> from collections import deque
#>>> d = deque()
#>>> d.append(1)
#>>> print d
deque([1])
#>>> d.appendleft(2)
#>>> print d
deque([2, 1])
#>>> d.clear()
#>>> print d
deque([])
#>>> d.extend('1')
#>>> print d
deque(['1'])
#>>> d.extendleft('234')
#>>> print d
deque(['4', '3', '2', '1'])
#>>> d.count('1')
1
#>>> d.pop()
'1'
#>>> print d
deque(['4', '3', '2'])
#>>> d.popleft()
'4'
#>>> print d
deque(['3', '2'])
#>>> d.extend('7896')
#>>> print d
deque(['3', '2', '7', '8', '9', '6'])
#>>> d.remove('2')
#>>> print d
deque(['3', '7', '8', '9', '6'])
#>>> d.reverse()
#>>> print d
deque(['6', '9', '8', '7', '3'])
#>>> d.rotate(3)
#>>> print d
deque(['8', '7', '3', '6', '9'])
Task

Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format

The first line contains[0] an integer , the number of operations.
The next  lines contains[0] the space separated names of methods and their values.

Constraints


Output Format

Print the space separated elements of deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
'''

n=int(input())
lst1=[]
for i in range(n):
    lst1.append(input())


lstres=[]
for i in lst1:
    ins=[val1 for val1 in i.split() if val1.isalpha()]
    val=[int(val2) for val2 in i.split() if val2.isdigit()]
    if ins[0]=="append":
        lstres.append(val)
    if ins[0]=="appendleft":
        lstres.insert(0,val)
    if ins[0]=="clear":
        lstres.clear()
    if ins[0]=="extend":
        lstres.extend(val)
    if ins[0]=="extendleft":
        lstres.extend(val)
    if ins[0]=="count":
        print(lstres.count(val))
    if ins[0]=="pop":
        lstres.pop()
    if ins[0]=="popleft":
        lstres.pop(0)
    if ins[0]=="remove":
        lstres.remove(val)
    if ins[0]=="reverse":
        lstres = lstres.reverse()
    if ins[0]=="rotate":
        lstres[val:]=lstres[:val]

for i in lstres:
    for j in i:
        print(j,end=" ")