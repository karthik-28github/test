#if you enter a name it should give whhich the correspodning row the element is available

key=["qwertyuiop","asdfghjkl","zxcvbnm"]
name1=input("enter the name")
name=name1.lower()

stroke=""
for i in name:

    if i in key[0]:
        stroke=stroke+" 1"
        # name.pop(0)
    if i in key[1]:
        stroke = stroke + " 2"
        # name.pop(0)
    if i in key[2]:
        stroke = stroke + " 3"
        # name.pop(0)

print(stroke)

