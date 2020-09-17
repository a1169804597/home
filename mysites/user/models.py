from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='昵称')
    nickname=models.CharField(max_length=20)

    def __str__(self):
        return '%s(%s)'%(self.user.username,self.nickname)
