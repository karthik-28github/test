#916. Word Subsets
import re
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
flag=False
for i in words2:
    for j in words1:
        if j:
            if i in j :
                 flag=True
            else:
                flag=False




