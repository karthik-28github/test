#the program to accept date of birth and give the corresponding day in week
import calendar
import datetime
day_name=["Monday","tuesday","wednesday","Thursday","Friday","Saturday","Sunday"]
year=int(input("enter the year of birth"))
month=int(input("enter the month of the birth"))
day=int(input("enter the date of birth"))
# print(calendar.day_name(year,month,day))
date1=datetime.date(year,month,day)
week_day=date1.weekday()
print("you are born on ",day_name[week_day])
