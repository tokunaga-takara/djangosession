from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField('user name', max_length=15)
    micropost = models.CharField('tweet', max_length=140, blank=True)

    def __str__(self):
        return self.name


class Login(models.Model):
    username = models.CharField('username', max_length=15)
    password = models.CharField('password', max_length=20)

    def __str__(self):
        return self.username