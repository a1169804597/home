#@功能：
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNum

def read_statistics_one_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)  # 得到模型对象
    key="%s_%s_read"%(ct.model,obj.pk)           #创建Cookies的键
    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # 存在记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)  # 得到阅读集合对象
            # 不存在
        else:
            readnum = ReadNum(content_type=ct, object_id=obj.pk)  # 不存在得到的是原始的博客计数对象
        readnum.read_num += 1
        readnum.save()
    return key