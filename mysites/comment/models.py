from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    # content_type是模型的名称如blog
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    # 博客的ID
    object_id = models.PositiveIntegerField()
    # 是把博客的ID和模型封装的对象
    content_object = GenericForeignKey('content_type', 'object_id')

    text=models.TextField()   #评论的文本
    comment_time=models.DateTimeField(auto_now_add=True) #评论的时间
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)



