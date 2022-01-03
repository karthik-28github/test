def countdown(num):
    print(num)
    if num==0:
        return
    else:
        countdown(num-1)

n=int(input("enter the max count down number"))
countdown(n)
