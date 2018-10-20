from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=512)
    confirm_passwd = models.CharField(max_length=512)

    def __str__(self):
        return self.username