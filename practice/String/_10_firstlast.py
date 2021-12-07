str =input("enter the string")
start = str[0]
end = str[-1]
swapped_str = end+str[1:-1]+start
print(swapped_str)