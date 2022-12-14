from django.db import models
from django.utils import timezone


# Create your models here.
class Department(models.Model):
    departname = models.CharField(verbose_name='部门名称', max_length=16, unique=True)
    createdate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    class Meta:
        verbose_name = '部门表'
        verbose_name_plural = verbose_name

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
    username = models.CharField(verbose_name='用户名称', max_length=16, unique=True)
    depart = models.ForeignKey(verbose_name='所在部门', to=Department, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField(verbose_name='状态', choices=STATUS, default=None, null=True)
    createdate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)

    class Meta:
        verbose_name = '人员基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Computer(models.Model):
    brand_choices = (
        (0, '联想'),
        (1, '惠普'),
    )
    brand = models.SmallIntegerField(verbose_name='品牌', choices=brand_choices, default=0)
    computer_type = models.CharField(max_length=16, verbose_name='型号', null=True)
    serial_number = models.CharField(max_length=32, verbose_name='序列号', unique=True)
    # 生成字段 owner_id
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True,
                              verbose_name='拥有者',
                              related_name='owners')
    production_date = models.DateField(verbose_name='生产日期', default=timezone.now)
    mac_addr = models.CharField(max_length=14, default=None, verbose_name='MAC地址')
    mod_time = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    img = models.FileField(verbose_name='图片', upload_to='computer/', blank=True, null=True)

    class Meta:
        verbose_name = '电脑'
        verbose_name_plural = verbose_name


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class IpAddr(models.Model):
    ip_addr = models.CharField(verbose_name='IP地址', max_length=16)
    mac_addr = models.CharField(verbose_name='MAC地址', max_length=14)
    interface = models.CharField(verbose_name='接口', max_length=16)
    cap_datetime = models.DateTimeField(verbose_name='采集时间')

    class Meta:
        # 模型对象返回的记录结果按照哪个字段排序
        ordering = ['cap_datetime']
        # 模型类在后台管理中显示的名称
        verbose_name = 'ARP表'
        verbose_name_plural = verbose_name
