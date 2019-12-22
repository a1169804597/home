from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from . models import Blog,BlogType

# Create your views here.


def blog_list(request):
    blogs_all_list=Blog.objects.all()       #的到所有的博客
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
    context['blogs']=page_of_blogs.object_list
    context['page_of_blogs']=page_of_blogs
    context['blog_types']=BlogType.objects.all()
    context['page_range']=page_range
    context['blogs_count']=Blog.objects.all().count()
    return render_to_response('blog_list.html',context)

def blog_detail(request,blog_pk):
    context={}
    context['blog']=get_object_or_404(Blog,pk=blog_pk)
    return render_to_response('blog_detail.html',context)
def blogs_with_type(request,blog_type_pk):
    blog_type=get_object_or_404(BlogType,pk=blog_type_pk)      #通过主键得到是哪一个博客类型
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)  #得到分类后的所有博客
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)  # 每多少篇进行分页
    page_num = request.GET.get('page', 1)  # 获取页码参数
    page_of_blogs = paginator.get_page(page_num)  # 当前页的博客对象
    current_page_num = page_of_blogs.number  # 获取当前的页码
    # 获取当前页面和前后各两页
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(
        range(current_page_num, min(current_page_num + 3, page_of_blogs.paginator.num_pages + 1)))
    range(current_page_num, min(current_page_num + 3, page_of_blogs.paginator.num_pages + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blog_type'] = blog_type                   #当前博客列表的类型
    context['blogs'] = page_of_blogs.object_list       #分类后的所有博客
    context['page_of_blogs'] = page_of_blogs           #当前页博客对象
    context['page_range'] = page_range                 #当前页和前后各2页
    context['blog_types'] = BlogType.objects.all()     # 博客的所有分类
    context['blogs_count'] = Blog.objects.all().count()#博客数量
    return render_to_response('blog/blog_with_type.html',context)