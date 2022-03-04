lst1=["()",")(()))","(","(()((()())()))","t)(est","hi())(","(hello))","hello","(hell(0))",")(","((()))","he()(((ll)))"]
for i in lst1:
    count1 = 0
    count2 = 0
    if "(" in i:
        first=i.find("(")
        count1=i.count("(")
    if ")" in i:
        second=i.find(")",-1)
        count2=i.count(")")
    print(first,second)
    print(i,end="->")
    if count1==count2 and i.endswith("(")!=True and i.startswith(")")!=True and first<second:
        print(True)
    else:
        print(False)