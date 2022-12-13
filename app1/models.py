from django.db import models


# Create your models here.
class Department(models.Model):
    departname = models.CharField(verbose_name='部门名称', max_length=16)
    createdate = models.DateTimeField(verbose_name='创建日期', )


class User(models.Model):
    username = models.CharField(verbose_name='用户名称', max_length=16)
    depart = models.ForeignKey(to=Department,on_delete=models.DO_NOTHING)
    status = models.CharField(verbose_name='状态', max_length=1)
    createdate = models.DateTimeField(verbose_name='创建日期', )

    class Meta:
        verbose_name = '人员基本信息'


class Computer(models.Model):
    brand = models.CharField(max_length=16)
    computer_type = models.CharField(max_length=16)
    serial_number = models.CharField(max_length=32)
    owner = models.ForeignKey(to=User,on_delete=models.DO_NOTHING)
