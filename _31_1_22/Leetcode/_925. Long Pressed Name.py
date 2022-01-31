#925. Long Pressed Name
'''Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 '''

class Solution:
  def isLongPressedName(self, name: str, typed: str) -> bool:
    i = 0

    for j, t in enumerate(typed):
      if i < len(name) and name[i] == t:
        i += 1
      elif j == 0 or t != typed[j - 1]:
        return False

    return i == len(name)

s=Solution()
name="karthik"
name1="kkarthhik"
res=s.isLongPressedName(name,name1)

print("the name pressed long",res)