from django.shortcuts import render


def index(request):
    data = {'title': 'Analytics'}
    return render(request, 'analytics/index.html', context=data)


def start(request):
    data = {'title': 'Analytics'}
    return render(request, 'analytics/analytics.html', context=data)
