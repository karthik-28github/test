a=0
b=2
try:
    c=a+d
    raise NameError
except NameError as e:
    print(e)