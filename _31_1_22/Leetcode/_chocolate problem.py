#cholocate problem
#19
#251344351121413421
#18,7

chocolate=[2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
sum=18
max=7

sum1=0
count=0
i=0
while i!=len(chocolate):

    for i in range(len(chocolate)):
        sum1 = 0
        print(i)
        for j in range(max):
            sum1+=chocolate[i]
        print(sum1)
        print("------")
        if sum1==sum:
            count+=1
        else:
            print("hai")
            i=i-max+1
            print(i)


print(count)

