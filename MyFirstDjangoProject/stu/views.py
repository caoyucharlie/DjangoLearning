# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from stu.models import Student

# Create your views here.
def addStudent(request):
    print(request)
    stu = Student()
    stu.name = '张三'
    stu.sex = 1
    stu.save()
    return HttpResponse('添加成功')

def boy_hello(request):
    return HttpResponse('hello boy')