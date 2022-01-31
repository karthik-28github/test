#970. Powerful Integers

x=2
y=3
bound=10
result=0
for i in range(bound):
    result=0
    for j in range(bound):
        if x*i+y*j<bound:

            print(x*i+y*j,"=",end=" ")
            print(x,"^",i,"(",x*i,")+",y,"^",j,"(",y*j,")")
