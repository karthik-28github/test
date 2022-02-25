#palandrome of a givin number
import itertools
from itertools import permutations
def palindromes(lst):
    results=[]
    for text in lst:
        if text == text[::-1]:
            results.append(text)
    return results

n=int(input("enter the number "))

lst=[]
perm = itertools.permutations(str(n),len(str(n)))
for i in perm:
    a=list(i)
    str1="".join(a)
    lst.append(str1)

res = palindromes(lst)

res=set(res)
if len(res)==0:
    print(-1)
else:
 pass