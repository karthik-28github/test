#712. Minimum ASCII Delete Sum for Two Strings

#
# s1=input("enter the first string")
# s2=input("enter the second string")
s1="sachin"
s2="karthi"
sum = 0
s3 = s2
s4 = s1
for i in s1:
    if i not in s3:
        sum += ord(i)
    else:
        s3 = s3.replace(i, "")
for j in s2:
    if j not in s4:
        sum += ord(j)
    else:
        s4 = s4.replace(j, "")
print(sum)

