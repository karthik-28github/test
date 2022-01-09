#number of digit 1 availble which is greater than 0 and less than or equal to the n
# it give how many dit 1 is availble
#exp     if n=10      we have 1 to 10   --> 1 has 1 and 10 has 1



class Demo:
    def __init__(self):
        pass
    def pntcnt(self):
        pass



d=Demo()

count=0
num=input("enter the number ")

for i in range(int(num)):
    for j in str(i):
        if int(j)==1:
            count+=1

print("the no of 1's available from 0 to",num,"is ",count)
