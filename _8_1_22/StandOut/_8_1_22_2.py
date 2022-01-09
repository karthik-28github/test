#nim game
#you can pic 1/2/3 stones at a time
# the person who pics the last stone will will the game

import random

num=int(input("enter the number of stones"))
player1="karthik"
player2="Friend"


stones=[]
for i in range(1,num+1):
    stones.append(i)

while len(stones)!=0:
    try:
        print(stones)
        n1=int(input("enter a number to pic the stones"))
        for i in range(n1):
            stones.pop()
        print(stones)
        if len(stones)==0:
            print(player1,"wins")
            break
        n2=random.randint(1,3)
        if len(stones)<=3:
            n2=len(stones)
        print(n2)
        if(n2>len(stones)):
            print(n2,"greater than",len(stones))
            continue
        for i in range(n2):
            stones.pop()
        if len(stones)==0:
            print(player2,"wins")
            break
    except Exception as e:
        print("invalid pick")
