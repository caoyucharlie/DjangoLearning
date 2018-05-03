这个登录界面，在之前的之上，做了一些修改</br>
注释掉了utils里的UserAuthMiddleware的中间件，改用django自带的登录验证(uauth中)</br>
即在uauth/views里的djlogin,djregist,djlogout三个方法</br>
在setting 143行，LOGIN_URL = '/uauth/dj_login/'设置登录跳转的地址，如果没有login，登录任何地址就会跳到dj_login这个地址里</br>
在utils里，新建VisitTimesMiddleWare，并且在setting里MIDDLEWARE 53行中增加中间件，该功能用于实现统计点击次数到数据库，在此之前，在stu.model里创建了Visit，并且makemigrations到数据库里，每当有点击行为，数据库相应的次数增加1.</br>

restful风格，是所有Web应用都应该遵守的架构设计指导原则(Representational State Transfer,表现层状态转化)</br>

用reset_framework 替代原来自己写的增删改查功能，在stu里创建serializers的py文件，setting里增加'rest_framework',并且在stu.views里面from rest_framework.routers import SimpleRouter，增加url。最后只需在views文件里面增加第72-80行代码，即可实现。

在setting里，创建日志路径。


