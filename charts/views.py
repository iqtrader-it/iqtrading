from django.shortcuts import render

def index(request):
    data = {'title': 'TradingView'}
    return render(request, 'analytics/index.html', context=data)

def start(request):
    data = {'title': 'TradingView'}
    return render(request, 'charts/charts.html', context=data)
