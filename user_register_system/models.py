from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,default='')
    gender = models.CharField(max_length=10)
    address = models.TextField(null=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=50)
    def __str__(self):
        return self.name
