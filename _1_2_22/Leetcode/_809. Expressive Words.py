#809. Expressive Words

str1 = "heeellooo"
words = ["hello", "hi", "helo"]


count=0
dict1={}
dict2={}
for i in str1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
for j in words:
    for k in j:
        if j not in dict2:
            dict2[k]=1
        else:
            dict2[k]+=1
    for j,k in dict1.items():
        for m,n in dict2.items():
            if j==m:
                print(j)
                if k<=n:
                    print(k)






