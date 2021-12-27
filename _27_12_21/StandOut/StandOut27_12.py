#snake and ladder game
import random

def ladder(l):
    a=random.randint(1,10)
    if l+a>100:
        print("the random no is",a)
        print("the score will go beyod 100 ")
        print("the score is increases by 0 only")
        return 0
    else:
        print("the score is incresed by",a)
        return a


def snake(s):
    b=random.randint(1,10)
    if s-b<0:
        print("the random no is",b)
        print("the score will go below 0")
        print("score is reduced by 0 only")
        return 0
    else:
        print("score is reduced by",b)
        return b




player1=input("enter the player 1 name")
player2=input("enter the player 2 name")
p1=0
p2=0
desti=100
lad=[5,15,25,35]
snk=[10,20,30,40]
# lad=[14,19,27,39,55,63,89]
# snk=[23,35,49,62,85,93,99]
# a1=random.randint(1,6)
# b1=random.randint(1,6)
board=[i for i in range(1,100)]
count=0
while(p1 or p2 <100):
    print("--------------------------------------\n")
    p1=p1+random.randint(1,6)
    print(player1, "score is", p1)
    for p1 in snk:
        print(player1, "score is", p1)
        print(player1,"bitten by a snake")
        p1=p1-snake(p1)
        print(player1,"fell down to to",p1)

    for p1 in lad:
        print(player1, "found a ladder")
        p1=p1+ladder(p1)
        print(player1, "claimed to", p1)
    print("--------------------------------------\n")
    p2=p2+random.randint(1,6)
    print(player2, "score is", p2)
    for p2 in snk:
        print(player1, "score is", p2)
        print(player2, "bitten by a snake")
        p2=p2-snake(p2)
        print(player2, "went to", p2)
    for p2 in lad:
        print(player2, "score is", p2)
        print(player2, "found a ladder")
        p2=p2+ladder(p2)
        print(player2, "claimed to", p2)

    print(player1,"score is",p1)
    print(player2,"score is",p2)
    if p1 or p2 ==100:
        break


if p1==desti:
    print(player1,"has reached",desti,"first so he is the winner")
    print(player1,"took",count,"no of rotation to win this game")
else:
    print(player2,"has reached",desti,"first so he is the winner")
    print(player2, "took", count, "no of rotation to win this game")


