from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=100)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=5)
