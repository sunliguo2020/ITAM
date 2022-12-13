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
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 电脑显示页面
    path('computer/list/', views.computer_list),
    path('computer/<int:nid>/edit/', views.computer_edit),
    # 电脑添加页面
    path('computer/add/', views.computer_add),

    # 用户管理
    path('user/list/',views.user_list),
    path('user/add/',views.user_add),

    # 部门管理
    path('dep/list/', views.dep_list),
    path('dep/add/', views.dep_add),
]
