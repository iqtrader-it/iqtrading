from django.shortcuts import render

def index(request):
    data = {'title': 'Forum'}
    return render(request, 'analytics/index.html', context=data)

def start(request):
    data = {'title': 'Forum'}
    return render(request, 'forum/forum.html', context=data)
