from django.urls import path
from . import views

# aaa.urls << url들의 정보

urlpatterns = [
    path('', views.index, name='startIndex'),
]

