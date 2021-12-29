def winner(a):
    if a=="X":
        print("player who have entered X has won the match")
    elif a=="O":
        print("player who have entered O has won the match")
val=["X","O"]
def check(val):
    for i in val:
        if d3[1] == i and d3[2] == i and d3[3] == i:
            winner(i)
        elif d3[4] == i and d3[5] == i and d3[6] == i:
            winner(i)
        elif d3[7] == i and d3[8] == i and d3[9] == i:
            winner(i)
        elif d3[1] == i and d3[4] == i and d3[7] == i:
            winner(i)
        elif d3[2] == i and d3[5] == i and d3[8] == i:
            winner(i)
        elif d3[3] == i and d3[6] == i and d3[9] == i:
            winner(i)
        elif d3[1] == i and d3[5] == i and d3[9] == i:
            winner(i)
        elif d3[7] == i and d3[5] == i and d3[9] == i:
            winner(i)


flag=True
count=0
d1={}
d2={}

while(flag):
    p1=int(input("player1 enter a number(1-9)"))
    if p1 not in d1 or d2:
        d1[p1]="X"
        count += 1
        if count >= 9:
            flag = False
    else:
        continue

    if(flag):
        p2 = int(input("palyer 2 enter a number(1-9)"))
        if p2 not in d1 or d2:
            d2[p2] = "O"
            count+=1
            if count >= 9:
                flag = False
        else:
            continue
print(d1)
print(d2)
d3=dict(d1 | d2)
print(d3)
d4=dict(sorted(d3.items(),key=lambda x:x[0]))
print(d4)

for i,j in d4.items():
    if i==1:
        print(j,end="    ")
    if i==2:
        print(j,end="    ")
    if i==3:
        print(j,end="    ")
        print("\n")
    if i == 4:
        print(j,end="    ")
    if i == 5:
        print(j,end="    ")
    if i == 6:
        print(j,end="    ")
        print("\n")
    if i == 7:
        print(j,end="    ")
    if i == 8:
        print(j,end="    ")
    if i == 9:
        print(j,end="    ")
value=d3.values()
check(val)

    # var=f'''
    # {p1 or p2}    {p1 or p2}    {p1 or p2}
    # {p1 or p2}    {p1 or p2}    {p1 or p2}
    # {p1 or p2}    {p1 or p2}    {p1 or p2}
    # '''
# print(var)

