from django.db import models

# Create your models here.
class Register(models.Model):
    firstname = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)
    studing = models.CharField(max_length=10,null=True)
    bloodgroup = models.CharField(max_length=100,null=True)

class RegisterPrincipal(models.Model):
    email = models.EmailField()
    password1 = models.CharField(max_length=100)
