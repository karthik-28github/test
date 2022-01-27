#_Exchange Seats

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Karthi@28",
    database="new"
)

mycursor=mydb.cursor()

# mycursor.execute("create database new")

# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)

# mycursor.execute("create table students(id varchar(10),name varchar(10))")

# mycursor.execute("show tables")

# for x in mycursor:
#     print(x)

# sql="insert into students(id,name) values (%s,%s)"
#
# val1=("karthik","28")
# val2=("sachin","50")
# val3=("abhi","60")
# mycursor.execute(sql,val1)
# mycursor.execute(sql,val2)
# mycursor.execute(sql,val3)
# mydb.commit()

# sql = "INSERT INTO students (id, name) VALUES (%s, %s)"
# val = [
#   ( '4','Peter'),
#   ('652','Amy'),
#   ( '21','Hannah'),
#   ('345','Michael'),
#   ('2','Sandy'),
#   ('1','Betty'),
#   ('331','Richard'),
#   ('98','Susan'),
#   ('2','Vicky'),
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycur

# mycursor.execute("select * from students")
# result=mycursor.fetchall()
#
# for x in result:
#     print(x)

mycursor.execute("delete * from students")

