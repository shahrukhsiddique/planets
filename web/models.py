from django.db import models
from django.conf import settings


# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    created_on =  models.DateTimeField(auto_now=True)
    verified =  models.BooleanField(default=False)


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=f'profile',max_length=250,unique=True)
    created = models.DateField(auto_now_add=True)


def __str__(self):
    return self.user.username