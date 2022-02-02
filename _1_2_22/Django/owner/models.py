from django.db import models

# Create your models here.
class Credential(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)


class Item(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    quantity=models.FloatField()


