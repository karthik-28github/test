total=0
def myfun(filled_bottle,exchangerate):
    global total
    total+=filled_bottle
    empty_bottle=filled_bottle
    if(empty_bottle>=exchangerate):
        filled_bottle=empty_bottle/exchangerate
        return myfun(filled_bottle,exchangerate)
    else:
        return total


res=myfun(10001,2)
print(res)