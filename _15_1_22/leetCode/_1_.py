#enter n number of elements
#when ever you press any key except number it will stop taking inputs
#it will sort the number what ever you have entered
#it will ask you whether you want to know the position
#if you press yes or y   it will ask for which number
#it will give the postion of the number
#if you press no or n it will print all the number which you have entered in a sorted manner



list1=[]
while(True):
    try:

        a=int(input("enter the number "))
        list1.append(a)

    except Exception as e:
        print("enter only number \n previous numbers are considered for the search")
        break
list1.sort(reverse=False)
d={}
j=1
for i in list1:
    if j not in d:
        d[j]=i
        j+=1
print("............................................................................................")
opt=input("do u wanna know  element's position Y(Yes)/N(No) after Sorting")
if opt.lower()=='y' or opt.lower()=='yes':
    ele=int(input("enter the number"))
    for k,l in d.items():
        if l==ele:
            print("after sorting  your element is placed at",k,"position")
            print("............................................................................................")
            break
    else:
        print("you not entered ", ele, "previously")
        print("............................................................................................")
else:
    print("the elements you have entered after sorting are")
    for y, z in d.items():
        print(z, end=" ")
    print("............................................................................................")

for y, z in d.items():
    print(z, end=" ")
print("\n")
print("............................................................................................")

