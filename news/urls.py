from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', catalog),
    path('catalog', catalog),
    path('add', add),
    path('add_ajax', add_ajax),
    re_path(r'^show/(?P<post_id>[0-9]+)$', show),
    re_path(r'^delete/(?P<post_id>[0-9]+)$', delete),
    re_path(r'^update/(?P<post_id>[0-9]+)$', update),
]

