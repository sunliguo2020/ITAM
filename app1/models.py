import datetime
import time

from django.db import models
from django.utils import timezone


# Create your models here.
class Department(models.Model):
    departname = models.CharField(verbose_name='部门名称', max_length=16, unique=True)
    createdate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    def __str__(self):
        return self.departname


class User(models.Model):
    """
    人员管理
    """
    STATUS = (
        (None, '请选择'),
        (0, '正常'),
        (1, '失效'),
    )
    username = models.CharField(verbose_name='用户名称', max_length=16,unique=True)
    depart = models.ForeignKey(verbose_name='所在部门', to=Department, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField(verbose_name='状态', choices=STATUS, default=None,null=True)
    createdate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    class Meta:
        verbose_name = '人员基本信息'

    def __str__(self):
        return self.username


class Computer(models.Model):
    brand_choices = (
        (0, '联想'),
        (1, '惠普')
    )
    brand = models.SmallIntegerField(verbose_name='品牌', choices=brand_choices)
    computer_type = models.CharField(max_length=16, verbose_name='型号',null=True)
    serial_number = models.CharField(max_length=32, verbose_name='序列号', unique=True)
    # 生成字段 owner_id
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, verbose_name='拥有者',related_name='owners')
    production_date = models.DateField(verbose_name='生产日期',default=timezone.now)
    mac_addr = models.CharField(max_length=14,default=None,verbose_name='MAC地址')
    mod_time = models.DateTimeField(verbose_name='最后修改时间',auto_now=True)