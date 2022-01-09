class String:
    def lexicography_str(self,str1):
        l2 = [x for x in sorted(str1.split(), reverse=False)]
        str2 = " ".join(l2)
        print(str2)

str1='sachin is good india bangalore apple bullet shine country'
s1=String()
s1.lexicography_str(str1)