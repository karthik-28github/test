#_917. Reverse Only Letters

class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

s=Solution()
val= "Test1ng-Leet=code-Q!"

print(s.reverseOnlyLetters(val))


