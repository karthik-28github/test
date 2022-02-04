#762. Prime Number of Set Bits in Binary Representation

m=int(input("Enter the left number "))
n=int(input("enter the right number"))
count=0
new=[]
for i in range(m,n+1):
    bi=bin(i)
    str1=bi[2:]
    new.append(str1)

for j in new:
    print(j)
    if j.count("1")>=2:
        count+=1

print(count,"numbers have prime number of bits")