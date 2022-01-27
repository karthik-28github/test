# 627 sql operations
#create table employee with id name sal designtaion
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Karthi@28",
    database="new2",

)

mycursor=mydb.cursor()

# mycursor.execute("create database new2")

# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)
#
# mycursor.execute("create table employee(id varchar(10),name varchar(30),salary int(10),designation varchar(20)) ")
#
# mycursor.execute("show tables")
#
# for x in mycursor:
#     print(x)
#
# sql="insert into employee(id,name,salary,designation) values(%s,%s,%s,%s)"
# data=("28","karthik",20000,"eng")
#
# mycursor.execute(sql,data)
#
# mydb.commit()
#
# mycursor.execute("select * from employee")
#
# data1=mycursor.fetchall()
# for i in data1:
#     print(i)

# sql="insert into employee(id,name,salary,designation) values(%s,%s,%s,%s)"
# data1=[("28","karthik",20000,"eng"),
#       ("29","karthi",250000,"eng")
#       ]
# mycursor.executemany(sql,data1)
# mydb.commit()

mycursor.execute("select * from employee")

for x in mycursor:
    print(x)


