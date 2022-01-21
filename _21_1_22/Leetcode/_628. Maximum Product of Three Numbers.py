#628. Maximum Product of Three Numbers

num=[2,4,5,6,7]
product=1
result=0
for j in range(len(num)):
    for i in num[:3]:
        product=product*i
    result=max(product,result)
    print(product)
    product=1
    num=num[1:]+num[:1]

print("the MAX of product of 3 numbers is",result)