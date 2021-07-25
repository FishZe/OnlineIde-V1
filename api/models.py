from django.db import models

# Create your models here.
class Users(models.Model):
    
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    number = models.IntegerField()


