#Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

#Note that the letters wrap around.

#For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


lst=["d","e","f","g"]
val=(input("enter a character"))


for i in lst:
    if ord(i)>ord(val):
        print(i)
        break
