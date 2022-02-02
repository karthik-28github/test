from django.db import models

# Create your models here.
class Credential(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)

    def authenticate(self,email,password):
        self.email=email
        return email

    def login(self,email):
        self.email=email
        return email

    def logout(self,email):
        return " "
class Item(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    quantity=models.FloatField()



