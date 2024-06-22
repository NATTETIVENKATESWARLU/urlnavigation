from django.urls import path
from .views import *
app_name='abc'


urlpatterns=[
    path('a/',A,name='a'),
    path('b/',B,name='b'),
]