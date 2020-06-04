from django.shortcuts import render
from news.models import Blog
from news.models import Category

def about(request):
    return render(request,'about.html')

def main(request):
    data = Category.objects.all()
    data2=Blog.objects.all()
    context={
        'category':data,
       'blog':data2
    }
    return render(request,'web/index.html',context)

def morenews(request,id):
    blog=Blog.objects.all()
    context={
       'blogs':blog
    }
    return render(request,'web/singlepage.html')