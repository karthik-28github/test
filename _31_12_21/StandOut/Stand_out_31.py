#stand out problem
#stone paper scissor
import random

player1="You"
player2="Bot"
things=["ROCK","PAPER","SCISSOR"]

while True:
    try:
        p1=int(input("Enter the number 1(rock)  2(paper)  3(scissor)"))
        p1-=1
        p2=random.randint(0,2)
        print(things[p1],end="    ")
        print(things[p2])
        if p1==p2:
            print(things[p1],"and",things[p2]," its a Draw")
        if p1==0 and p2==1:
            print(things[p1], "and", things[p2],player2,"Won")
        if p1==0 and p2==2:
            print(things[p1], "and", things[p2],player1,"Won")
        if p1==1 and p2==2:
            print(things[p1], "and", things[p2],player2,"Won")
        if p1==1 and p2==0:
            print(things[p1], "and", things[p2],player2,"Won")
        if p1==2 and p2==1:
            print(things[p1], "and", things[p2],player2,"Won")
        if p1==2 and p2==0:
            print(things[p1], "and", things[p2],player2,"Won")
        print("\n"*3)
        print("------------------------------------------------------")
        raise Exception
    except Exception as e:
        print(e)