from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

# Create your models here.
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    #content_type是模型的名称如blog
    content_type=models.ForeignKey(ContentType,on_delete=models.DO_NOTHING)
    #博客的ID
    object_id=models.PositiveIntegerField()
    #是把博客的阅读数量和模型封装的对象
    content_object=GenericForeignKey('content_type','object_id')

class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)  # 得到模型
            readnum=ReadNum.objects.get(content_type=ct,object_id=self.pk) #得到阅读集合对象
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

# 阅读详细
class ReadDetail(models.Model):
    date=models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)  # content_type是模型的名称如blog
    object_id = models.PositiveIntegerField() # 博客的ID
    content_object = GenericForeignKey('content_type', 'object_id')   # 是把博客的阅读数量和模型封装的对象