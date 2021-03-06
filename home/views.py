from django.shortcuts import render
from news.models import Post


def index(request):
    data = dict()
    data['title'] = 'Main page'
    data['posts'] = Post.objects.order_by('-id')[:3]
    return render(request, 'home/index.html', context=data)


def about(request):
    data = {'title': 'About'}
    return render(request, 'home/about.html', context=data)


def contacts(request):
    data = {'title': 'Contacts'}
    return render(request, 'home/contacts.html', context=data)
