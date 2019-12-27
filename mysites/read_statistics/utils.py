#@功能：
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from read_statistics.models import ReadNum,ReadDetail


def read_statistics_one_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)  # 得到模型对象
    key="%s_%s_read"%(ct.model,obj.pk)           #创建Cookies的键
    #阅读判断

    if not request.COOKIES.get(key):
        '''
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # 存在记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)  # 得到阅读集合对象
            # 不存在
        else:
            readnum = ReadNum(content_type=ct, object_id=obj.pk)  # 不存在实例化得到的是原始的博客计数对象
        '''
        readnum,created=ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        #总数据
        readnum.read_num += 1
        readnum.save()
    #阅读明细判断
    date=timezone.now().date()
    '''
    if ReadDetail.objects.filter(content_type=ct, object_id=obj.pk,date=date).count():
        readDetail=ReadDetail.objects.get(content_type=ct, object_id=obj.pk,date=date)
    else:
        readDetail=ReadDetail(content_type=ct, object_id=obj.pk,date=date)
    '''
    readDetail,created=ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk,date=date)
    readDetail.read_num+=1
    readDetail.save()
    return key

#前七天的阅读明细
def get_seven_days_read_data(content_type):
    today=timezone.now().date()
    dates=[]
    read_nums=[]
    for i in range(7,0,-1):
        date=today-datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details=ReadDetail.objects.filter(content_type=content_type,date=date)
        result=read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return read_nums ,dates
#今天热门博客
def get_today_hot_data(content_type):
    today=timezone.now().date()
    read_details=ReadDetail.objects.filter(content_type=content_type,date=today).order_by('-read_num')#今天阅读的博客由大到小排序
    return read_details[:7]
#昨天的热门博客
def get_yestereday_hot_data(content_type):
    today = timezone.now().date()
    yestereday=today-datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type, date=yestereday).order_by(
        '-read_num')  # 今天阅读的博客由大到小排序
    return read_details[:7]
#一周的热门博客
'''
def get_7_days_hot_data(content_type):
    today=timezone.now().date()
    date=today-datetime.timedelta(days=7)
    read_details=ReadDetail.objects.filter(content_type=content_type,date__lt=today,date__gte=date)\
        .values('content_type','object_id').annotate(read_num_sum=Sum('read_num')).order_by('-read_num')
    return read_details[:7]
'''