#_605. Can Place Flowers


flower=[1,0,0,0,0,1]
print(flower)
loc=int(input("enter the position where u need to plant the plant"))

for i in range(len(flower)):
    if flower[loc]==1:
        print("you have a plant at position ",loc)
        print("you cant plant here")
        break
    elif flower[loc]==0:
        if flower[loc-1]==0 and flower[loc+1]==0:
            print("the plant have been planted at pos",loc)
            flower[loc]=1
            print(flower)
            break
        else:
            print("u  have adjucent plant")
            print("print u cant plant here")
            break
    else:
        print("you dont have any plant here")



