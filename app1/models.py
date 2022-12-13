from django.db import models


# Create your models here.
class Department(models.Model):
    departname = models.CharField(verbose_name='部门名称', max_length=16,unique=True)
    createdate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    def __str__(self):
        return self.departname


class User(models.Model):
    username = models.CharField(verbose_name='用户名称', max_length=16)
    depart = models.ForeignKey(verbose_name='所在部门', to=Department, on_delete=models.DO_NOTHING)
    status = models.CharField(verbose_name='状态', max_length=1,default='',null=True,blank=True)
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
    computer_type = models.CharField(max_length=16, verbose_name='型号')
    serial_number = models.CharField(max_length=32, verbose_name='序列号',unique=True)
    # 生成字段 owner_id
    owner = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, verbose_name='拥有者')
