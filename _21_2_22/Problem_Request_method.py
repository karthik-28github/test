import requests
from mysql import connector

server=connector.connect(host='localhost',
                         database='request_method',
                         user='root',
                         password='Karthi@28')
cur=server.cursor()

response=requests.get('https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries')

header_list1=[]
data_list1=[]
for x in response.headers.items():
    a=x[0].replace('-','_')
    b=x[1].replace(',','.',5)
    header_list1.append(a)
    data_list1.append(b)
data_list=tuple(data_list1)
count=0
dict1=dict()
for i,j in zip(header_list1,data_list1):
    count+=1
    dict1[i]=j

header_list=tuple(header_list1)
print(dict1)
keys=dict1.keys()

ln=len(dict1)
print(ln)


query1=f'''create table request({header_list[0]} text(16383),{header_list[1]} text (16383),
{header_list[2]} text (16383),{header_list[3]} text (16383),{header_list[4]} text (16383),
{header_list[5]} text (16383),{header_list[6]} text (16383),{header_list[7]} text (16383),
{header_list[8]} text (16383),{header_list[9]} text (16383),{header_list[10]} text (16383),
{header_list[11]} text (16383),{header_list[12]} text (16383),{header_list[13]} text (16383),
{header_list[14]} text (16383),{header_list[15]} text (16383),{header_list[16]} text (16383),
{header_list[17]} text (16383),{header_list[18]} text (16383),{header_list[19]} text (16383),
{header_list[20]} text (16383),{header_list[21]} text (16383))'''

query2=f''' insert into request values {data_list}'''
try:
    cur.execute(query2)
    server.commit()
    cur.close()
except Exception as e:
    print(e)

