from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Features(models.Model):
#     name = models.CharField(max_length=100)
#     details = models.CharField(max_length=500)

# class More(models.Model):
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     email = models.CharField(max_length=100, unique=True)
    # nationality = models.CharField(max_length=30, default=True)
    # phone = models.CharField(max_length=30, default= '+234')
    # state = models.CharField(max_length= 30, default=True)

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.user
    

