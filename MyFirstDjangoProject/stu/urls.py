# -*- coding:utf-8 -*-
from django.conf.urls import url
from stu import views



urlpatterns = [

    url(r'addstu/', views.addStudent),
    url(r'boy', views.boy_hello)
]
