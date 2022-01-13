from django.db import models


# Create your models here.
class Registration(models.Model):
    email=models.EmailField(max_length=50)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    mobilenumber=models.IntegerField()
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)