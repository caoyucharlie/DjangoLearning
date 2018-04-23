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
安装虚拟环境,方法二</br>
pip3 install django==1.11</br>
安装虚拟环境,方法三</br>
源码安装: tar -xvf django-1.11.8 tar.gz</br>
cd django-1.11.8</br>
(sudo) python3 setup.py install</br>
<h3>如果出现BadZipFile问题，则用pip install --no-cache-dir django==1.11命令解决</h3></br>




