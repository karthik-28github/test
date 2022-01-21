#557. Reverse Words in a String III
#program to reerse each word in a string
lst="Let's take LeetCode contest"

for i in lst.split(" "):
    print(i[::-1],end=" ")

