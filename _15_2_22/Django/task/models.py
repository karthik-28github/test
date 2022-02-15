from django.db import models

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    password1 = models.CharField(max_length=20)

class Tasks(models.Model):
    name=models.CharField(max_length=200)

