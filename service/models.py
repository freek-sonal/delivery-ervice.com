from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class category(models.Model):
    category=models.CharField(max_length=100,unique=True)
    add_date = models.DateTimeField('date added',default=timezone.now)

class restaurant(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    rest_name=models.CharField(max_length=100,unique=True)
    cons_date = models.DateTimeField('date added',default=timezone.now)
