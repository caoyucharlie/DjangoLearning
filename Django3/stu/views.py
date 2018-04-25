from django.http import HttpResponse
from django.shortcuts import render
from stu.models import Student, StudentInfo, GoodsUser,Goods
from grade.models import Grade
# Create your views here.


def addStu(request):
    if request.method == 'GET':
        return render(request, 'addstu.html')

    if request.method == 'POST':
        stu_name = request.POST.get('name')
        if request.POST.get('sex') == '男':
            stu_sex = 1
        else:
            stu_sex = 0
        stu_birth = request.POST.get('birth')
        stu_yuwen = request.POST.get('yuwen')
        stu_shuxue = request.POST.get('shuxue')

        Student.objects.create(
            stu_name=stu_name,
            stu_sex=stu_sex,
            stu_birth=stu_birth,
            stu_yuwen=stu_yuwen,
            stu_shuxue=stu_shuxue
        )
        return render(request, 'addstu.html')

def selStu(request):
    # 通过扩展表学生的地址去查找学生的信息
    # 查找addr＝？ 的学生信息
    # stus = StudentInfo.objects.filter(stu_addr='成都天府新区')
    # stu = StudentInfo.objects.filter(stu_addr__contains='成都天府新区')
    # stu = stus[0]
    # selstu = Student.objects.filter(id=stu.id)
    # stus = StudentInfo.objects.filter(stu_addr__contains='成都天府新区')
    # stu = stus[0]
    # selstu = stu.stu

    #通过学生表去查找学生拓展表信息
    # 查找stu_name＝狄仁杰的学生查找家庭住址
    stu = Student.objects.filter(stu_name='狄仁杰').first()
    selstu = stu.studentinfo
    return render(request, 'selstu.html', {'selstu': selstu})


def fselStu(request):
    # #查询python 班级下的学生
    # #方法一
    # g = Grade.objects.get(g_name='python')
    # stus = Student.objects.filter(g_id=g.id)
    # #方法二
    # # g = Grade.objects.get(g_name='python')
    # # g.student_set.all()
    # # 查询叫礼拜的同学的班级信息
    # stu = Student.objects.get(stu_name='马可波罗')
    # gs = stu.g

    # # 查询python班下语文成绩大于50分的学生
    # g = Grade.objects.get(g_name='python')
    # stus = g.student_set.filter(stu_yuwen__gte=50)

    # 查询python班级中出生在80后的男生的信息
    g = Grade.objects.get(g_name='python')
    stus = g.student_set.filter(stu_birth__gte='1980-01-01',
                         stu_birth__lt='1990-01-01',
                         stu_sex=1)

    return render(request, 'selgrade.html', {'stus': stus})


def manyGoods(request):
    # 获取小巧购买的商品
    u = GoodsUser.objects.filter(u_name='小乔')[0]
    goods = u.goods_set.all()
    # 获取购买哇哈哈用户的信息
    g = Goods.objects.get(g_name='哇哈哈')
    users = g.g_user.all()
    return render(request, 'goods.html', {'users': users})


def allStudent(request):
    stus = Student.objects.all()
    return render(request, 'all_stus.html', {'stus': stus})
