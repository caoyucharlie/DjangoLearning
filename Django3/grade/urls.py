

from django.conf.urls import url
from django.contrib import admin
from grade import views

urlpatterns = [
  url(r'^grades/', views.showGrades),
  url(r'show/', views.showpage)
]
