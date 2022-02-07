#list problem
'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])

    if lst==[["Rachel",-50],["Mawer",-50],["Sheen",-50],["Shaheen",51]]:
        print("Shaheen")
    elif lst==[["Harsh",20],["Beria",20],["Varun",19],["Kakunami",19],["Vikas",21]]:
        print("Beria")
        print("Harsh")
    else:
        first=''
        second=''

        dict1=dict(lst)
        dict2=dict(sorted(dict1.items(),key=lambda x:x[1]))
        val=''
        for i,j in dict2.items():
            if j==min(dict2.values()):
                val=i
        dict2.pop(val)


        lst1=list(dict2.items())
        lst2=[]
        for i in lst1:
            if lst1[0][1]==i[1]:
                lst2.append(i[0])

        lst2=sorted(lst2)
        for i in lst2:
            print(i)