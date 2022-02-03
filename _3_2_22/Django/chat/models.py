from django.db import models
from mysql import connector
# Create your models here.
server=connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="Karthi@28",
    database="chatapp"
)

def create_table(arg):
    query="create table 'arg' (message varchar)"
    cursor=server.cursor()
    cursor.execute(query)

create_table("8150901790")