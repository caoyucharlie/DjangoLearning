

from django.conf.urls import url
from django.contrib import admin
from stu import views

urlpatterns = [
    url(r'addstu/', views.addStu),
    url(r'sel/', views.selStu),
    url(r'fselstu', views.fselStu),
    url(r'manygoods/', views.manyGoods),
    url(r'^stu/', views.allStudent)
]
