from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from . models import Blog,BlogType

# Create your views here.
def get_blog_list_common_data(request,blogs_all_list):
    paginator=Paginator(blogs_all_list,settings.EACH_PAGE_BLOGS_NUMBER)   #每2篇进行分页
    page_num = request.GET.get('page', 1)  # 获取页码参数
    page_of_blogs=paginator.get_page(page_num) #当前一页的博客对象
    current_page_num=page_of_blogs.number #获取当前的页码
    #获取当前页面和前后各两页
    page_range=list(range(max(current_page_num-2,1),current_page_num))+ list(range(current_page_num,min(current_page_num+3, page_of_blogs.paginator.num_pages+1)))
    range(current_page_num,min(current_page_num+3, page_of_blogs.paginator.num_pages+1))
    # 加上省略页码标记
    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1]>=2:
        page_range.append('...')
    #加上首页和尾页
    if page_range[0] !=1:
        page_range.insert(0,1)
    if page_range[-1] !=paginator.num_pages:
        page_range.append(paginator.num_pages)

    context={}
    context['blogs']=page_of_blogs.object_list          #所有的博客
    context['page_of_blogs']=page_of_blogs              #当前页的对象
    context['page_range'] = page_range                  # 当前页和前后各2页
    context['blog_types'] = BlogType.objects.all()      # 博客所有的分类
    context['blog_dates'] = Blog.objects.dates('created_time', 'month', order='DESC')  # 按创建时间的倒序分类，按月筛选，返回月份的排序如2019年12月
    return context

def blog_list(request):
    blogs_all_list=Blog.objects.all()       #的到所有的博客
    context=get_blog_list_common_data(request,blogs_all_list)
    return render_to_response('blog_list.html',context)

def blogs_with_type(request,blog_type_pk):
    blog_type=get_object_or_404(BlogType,pk=blog_type_pk)      #通过主键得到是哪一个博客类型
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)  #得到分类后的所有博客
    context=get_blog_list_common_data(request,blogs_all_list)
    context['blog_type'] = blog_type                           #当前博客列表的类型
    return render_to_response('blog/blog_with_type.html',context)

def blogs_with_date(request,year,month):
    blogs_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)  # 得到通过时间筛选的博客
    context=get_blog_list_common_data(request,blogs_all_list)
    context['blogs_with_date']='%s年%s月'%(year,month)
    return render_to_response('blog/blogs_with_date.html', context)

def blog_detail(request,blog_pk):
    context={}
    blog=get_object_or_404(Blog,pk=blog_pk)                                                 #得到具体的某一篇博客
    context['previous_blog']=Blog.objects.filter(created_time__gt=blog.created_time).last() #下一条博客
    context['next_blog']=Blog.objects.filter(created_time__lt=blog.created_time).first()    #上一条博客
    context['blog']=blog
    return render_to_response('blog_detail.html',context)