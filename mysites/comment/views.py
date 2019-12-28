from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from comment.models import Comment

# Create your views here.

def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))  # 评论后跳转本页
    user=request.user
    #数据检查
    if not user.is_authenticated :
        return render(request, 'error.html', {'message': '用户未登入','redirect_to':referer})
    text=request.POST.get('text','').strip()
    if text=='':
        return render(request, 'error.html', {'message': '评论内容为空','redirect_to':referer})
    try:
        content_type = request.POST.get('content_type', '')  # 模型的名字blog
        object_id = int(request.POST.get('object_id', ''))  # 具体博客的ID
        model_class = ContentType.objects.get(model=content_type).model_class()  # 得到Blog
        model_obj = model_class.objects.get(pk=object_id)  # 得到具体某一篇博客对象
    except Exception as e:
        return render(request, 'error.html', {'message': '评论对象不存在','redirect_to':referer})
    #检查通过保存数据
    comment=Comment()
    comment.user=user
    comment.text=text
    comment.content_object =model_obj
    comment.save()
    return redirect(referer)
