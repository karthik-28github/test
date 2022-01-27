#1281. Subtract the Product and Sum of Digits of an Integer



n=int(input("enter a multiple digit number"))
product=1
sum=0
for i in str(n):
    product=product*int(i)
    sum=sum+int(i)

print("the sum of ",n,"is ",sum)
print("the product of ",n,"is ",product)
print("the result",product,"-",sum,"is",product-sum)
