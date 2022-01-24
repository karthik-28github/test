from django.db import models
import datetime
# Create your models here.
class Cabin(models.Model):
    name=models.CharField(max_length=20,null=True)
    mob=models.IntegerField(null=True)
    start=models.CharField(null=False,max_length=1000)
    end=models.CharField(null=False,max_length=1000)
    total=models.CharField(null=False,max_length=1000)