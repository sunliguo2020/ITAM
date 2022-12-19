"""ITAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from app1.views import computer, user, dep, account, admin, ip

app_name = 'app1'
urlpatterns = [
    path('', account.login),
    # path('admin/', admin.site.urls),

    # 登录
    path('login/', account.login),
    path('image/code/', account.image_code),

    path('logout/', account.logout),

    # 管理员
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 显示图片
    # re_path(r'meida/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    # 电脑显示页面
    path('computer/list/', computer.computer_list),
    # 电脑编辑
    path('computer/<int:nid>/edit/', computer.computer_edit),
    # 电脑添加页面
    path('computer/add/', computer.computer_add),
    # 电脑删除
    path('computer/<int:nid>/delete/', computer.computer_delete),
    path('computer/multi/', computer.computer_multi),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),
    path('user/multi/', user.user_multi),

    # 部门管理
    path('dep/list/', dep.dep_list),
    path('dep/add/', dep.dep_add),
    path('dep/<int:nid>/delete/', dep.dep_delete, name='dep_delete'),
    path('dep/<int:nid>/edit/', dep.dep_edit, name='dep_edit'),
    path('dep/multi/', dep.dep_multi),

    # Ip地址管理
    path('ip/list/', ip.ip_list),
    path('ip/add/', ip.ip_add),
    path('ip/<int:nid>/edit/', ip.ip_edit),
    path('ip/<int:nid>/delete/', ip.ip_delete),
    path('ip/multi/', ip.ip_multi),
]
