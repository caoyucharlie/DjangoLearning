
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rest_framework.routers import SimpleRouter
from stu import views

router = SimpleRouter()
router.register(r'student', views.StudentEdit)


urlpatterns = [

    url(r'index/', login_required(views.index)),
    url(r'addstu/', login_required(views.addStu), name='add'),
    url(r'addstuInfo/(?P<stu_id>\d+)/', login_required(views.addStuInfo), name='addinfo'),
    url(r'stupage/', login_required(views.stuPage))
]

urlpatterns += router.urls
