#747. Largest Number At Least Twice of Others


lst=[1,2,4,8]

flag=False
highest=max(lst)
lst.remove(highest)
print(lst)
for i in lst:
    if highest>=i+i:
        flag=True
    else:
        flag=False
lst.append(highest)
if flag:
    print(highest, "is the highest number among", lst, "which is greater or equal to double of all num")
else:
    print(-1, "no number is greater than equal to double of all number")
