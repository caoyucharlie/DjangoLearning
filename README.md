# DjangoProject
MVC-全称 Model View Controller,是模型-视图-控制器的缩写，用一种业务逻辑，数据，界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新缩写业务逻辑。</br>
<h4>优点：减低各个模块之间的耦合性，方便变更，更容易重构代码,最大程度实现了代码的重用</h4></br>
严格来说，django的模式应该是MVT模式，本质上和MVC没什么区别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同</br>
MVT- Model(负责业务与数据库(ORM)的对象) View(负责业务逻辑并适当调用Model和Template) Template(负责把页面渲染展示给用户)
注意: django中还有一个url粉发起，也叫做路由，主要用于将url请求发送给不同的view处理，view在进行组件相关业务逻辑处理</br>

安装虚拟环境,方法一</br>
pip3 install virtualenv</br>
创建一个文件夹，名称为env(mkdir env)，进入文件夹</br>
输入 virtualenv --no-site-packages testenv</br>
source activate激活虚拟环境后，再进行安装</br>
安装django环境,方法二</br>
pip3 install django==1.11</br>
安装django环境,方法三</br>
源码安装: tar -xvf django-1.11.8 tar.gz</br>
cd django-1.11.8</br>
(sudo) python3 setup.py install</br>
创建django工程</br>
django-admin startproject 文件名</br>
启动项目</br>
python manage.py runserver IP:端口</br>
__init__.py:初始化，配置pymysql链接的地方</br>
__setting__.py:配置信息的位置，databases等</br>
urls.py:处理发送过来的请求，找对应的方法(路由)</br>
wsgi.py: 网关</br>
创建app: python manage.py startapp app_name</br>
配置: settings.py文件中INSTALLED_APPS中写入创建的app的name。也可以导入app.py文件中的APPCONFIG下的name属性
模型: 在models.py文件中定义class 模型名称，继承models.Model
db_tables:定义数据库中的表名称
迁移: python manage.py makmigrations, python manage.py migrate
保持数据: stu= Student(), stu.name ='xxx', stu.save()
<h3>如果出现BadZipFile问题，则用pip install --no-cache-dir django==1.11命令解决</h3></br>




