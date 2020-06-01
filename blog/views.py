from django.shortcuts import render

def index(request):
    data = {'title': 'Blog'}
    return render(request, 'analytics/index.html', context=data)

def start(request):
    data = {'title': 'Blog'}
    return render(request, 'blog/blog.html', context=data)
