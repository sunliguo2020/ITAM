from django.db import models
from django.utils import timezone
from django.utils.html import format_html


# Create your models here.
class Department(models.Model):
    """
    部门管理
    """
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
    room_no = models.CharField(verbose_name='房间号', max_length=8, default=None, null=True,blank=True)
    status = models.SmallIntegerField(verbose_name='状态', choices=STATUS, default=None, null=True)
    createdate = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    last_mod_time = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)

    class Meta:
        verbose_name = '人员基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class BaseModel(models.Model):
    brand = models.SmallIntegerField(verbose_name='品牌', default=0)
    products_type = models.CharField(max_length=16, verbose_name='型号', null=True)
    serial_number = models.CharField(max_length=32, verbose_name='序列号', unique=True)
    # 生成字段 owner_id
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True,
                              verbose_name='拥有者',
                              related_name='owners')
    production_date = models.DateField(verbose_name='生产日期', default=timezone.now)
    mac_addr = models.CharField(max_length=14, default=None, verbose_name='MAC地址')

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        abstract = True


class Computer(models.Model):
    """
    电脑管理
    """

    brand_choices = (
        (0, '联想'),
        (1, '惠普'),
        (2, '组装'),
    )
    brand = models.SmallIntegerField(verbose_name='品牌', choices=brand_choices, default=0)
    computer_type = models.CharField(max_length=16, verbose_name='型号', null=True)
    serial_number = models.CharField(max_length=32, verbose_name='序列号', unique=True)
    # 生成字段 owner_id
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True,
                              verbose_name='拥有者',
                              related_name='computer_owners')
    production_date = models.DateField(verbose_name='生产日期', default=timezone.now)
    mac_addr = models.CharField(max_length=14, default=None, verbose_name='MAC地址')
    mod_time = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)
    img = models.FileField(verbose_name='铭牌图片', upload_to='computer/%Y/%m/', blank=True, null=True)
    mac_img = models.FileField(verbose_name='MAC地址图片', upload_to='MAC/%Y/%m/', blank=True, null=True)

    class Meta:
        verbose_name = '电脑'
        verbose_name_plural = verbose_name

    #  后台列表显示图片
    def computer_img(self):
        if self.img:
            return format_html(
                '<img src="/media/{}" width="156px" height="98px"/>',
                self.img,
            )
        else:
            return format_html(
                '<img src="/media/computer/none.jpg" width="156px" height="98px"/>',
            )

    def dis_mac_img(self):
        if self.mac_img:
            return format_html(
                '<img src="/media/{}" width="156px" height="98px"/>',
                self.mac_img,
            )
        else:
            return format_html(
                '<img src="/media/computer/none.jpg" width="156px" height="98px"/>',
            )


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class IpAddr(models.Model):
    """
    ip地址管理
    """
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


class Printer(BaseModel):
    """
    打印机管理
    """

    class Meta:
        verbose_name = '打印机'
        verbose_name_plural = verbose_name
