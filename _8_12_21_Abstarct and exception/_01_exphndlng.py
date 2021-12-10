#divion by  error

a=10
b=0

try:
    c=a/b

except Exception as e:
    print(e)
    print("invalid divider")

else:
    print(c)