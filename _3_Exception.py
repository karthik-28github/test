#Sort unique words alphanumerically
b=[]
a="abcde zfefw efg10 rtghf bfser"
try:
    for i in a.split():
        for j in i:
            print(j)
            if j.isnumeric()==True:
                raise ValueError
        print(i)
        b.append(i)
except ValueError as e:
    print(e)
print(b)
print(sorted(b))
