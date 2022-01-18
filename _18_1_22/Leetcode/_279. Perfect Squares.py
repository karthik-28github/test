#279. Perfect Squares

ps=[16,9,4,1]#these are the perfect sqaure number which is less than 10

n=int(input("enter a number "))
n1=n
m=0
for i in ps:
    if n%i==0:
        while(n!=0):
            n=n-i
            m+=1
        else:
            print(m,"=",end=" ")
            for j in range(m):
                print(i,"+",end=" ")
            break