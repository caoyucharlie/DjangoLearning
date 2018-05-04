from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from stu.models import Student, StudentInfo
from django.core.urlresolvers import reverse
from uauth.models import Users
from rest_framework import mixins, viewsets
from stu.serializers import StudentSerializer
# Create your views here.
import logging

logger = logging.getLogger('stu')


def index(request):
    # 获取所有学生信息
    # if request.method == 'GET':
    #     ticket = request.COOKIES.get('ticket')
    #     if not ticket:
    #         return HttpResponseRedirect('/uauth/login/')
    #     if Users.objects.filter(u_ticket=ticket).exists():
            stuinfos = StudentInfo.objects.all()
            logger.info('url: %s method:%s 获取学生信息成功' % (request.path, request.method))
            return render(request, 'index.html', {'stuinfos': stuinfos})
        # else:
        #     return HttpResponseRedirect('/uauth/login/')


def addStu(request):

    if request.method == 'GET':

        return render(request, 'addStu.html')
    if request.method == 'POST':
        # 跳转到学生页面
        name = request.POST.get('name')
        tel = request.POST.get('tel')

        stu = Student.objects.create(s_name=name, s_tel=tel)
        return HttpResponseRedirect(
            reverse('s:addinfo', kwargs={'stu_id': stu.id}))


def addStuInfo(request, stu_id):
    if request.method == 'GET':

        return render(request, 'addStuInfo.html', {'stu_id': stu_id})

    if request.method == 'POST':
       stu_id = request.POST.get('stu_id')
       addr = request.POST.get('addr')
       # 添加头像图片

       img = request.FILES.get('img')

       StudentInfo.objects.create(i_addr=addr, s_id=stu_id, i_image=img)

       return HttpResponseRedirect('/stu/index/')


def stuPage(request):

    if request.method == 'GET':

        page_id = request.GET.get('page_id', 1)
        stus = Student.objects.all()
        paginator = Paginator(stus, 3)
        page = paginator.page(int(page_id))
        return render(request, 'index_page.html', {'stus': page})


class StudentEdit(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    # 查询所有信息
    queryset = Student.objects.all()
    # 序列化
    serializer_class = StudentSerializer


def showStus(request):
    if request.method == 'GET':
        return render(request, 'show.html')
