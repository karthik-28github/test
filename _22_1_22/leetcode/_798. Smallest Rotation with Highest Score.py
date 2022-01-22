#798. Smallest Rotation with Highest Score

lst=12345
result=0
for i in str(lst):
    if str(lst[0])>str(lst[1]):
        result=result+1
    else:
        result=result+0
    lst=lst[1:]+lst[:1]

print(result)