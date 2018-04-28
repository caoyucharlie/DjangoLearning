from django.http import HttpResponseRedirect
from django.shortcuts import render
from stu.models import Student, StudentInfo
from django.core.urlresolvers import reverse
from uauth.models import Users
# Create your views here.


def index(request):
    # 获取所有学生信息
    if request.method == 'GET':
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/uauth/login/')
        if Users.objects.filter(u_ticket=ticket).exists():
            stuinfos = StudentInfo.objects.all()
            return render(request, 'index.html', {'stuinfos': stuinfos})
        else:
            return HttpResponseRedirect('/uauth/login/')


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

       StudentInfo.objects.create(i_addr=addr, s_id=stu_id)

       return HttpResponseRedirect('/stu/index/')
