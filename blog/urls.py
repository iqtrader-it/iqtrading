from django.urls import path
from .views import index, start
# from .views import *

urlpatterns = [
    path('', index),
    path('index', index),
    path('blog', start),
]
