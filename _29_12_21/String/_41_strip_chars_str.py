class String:
    def left_strip_str(self,str1):
        str2 = str1.lstrip('s')
        print(f'string after left strip is:{str2}')
    def right_strip_str(self,str1):
        str3 = str1.rstrip('n')
        print(f'string after right strip is:{str3}')
str1='ssssssssssssachinnnnnnnnnnnnnn'
str1=str1.lstrip('s')
print(str1)

s1=String()
s1.left_strip_str(str1)
s1.right_strip_str(str1)