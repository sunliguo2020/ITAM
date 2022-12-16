# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/13 11:54
"""
import re

from django import forms
from django.core.exceptions import ValidationError

from app1 import models
from .bootstrap import BootStrapModelForm, BootStrapForm
from app1.utils.encrypt import md5


class ComputerModelForm(BootStrapModelForm):
    img = forms.ImageField(required=False, label='铭牌照片')
    bootstrap_exclude_fields = ['img']

    class Meta:
        fields = ['brand',
                  'computer_type',
                  'serial_number',
                  'owner',
                  'production_date',
                  'mac_addr',
                  'img',
                  ]
        model = models.Computer
        labels = {
            'owner': '使用者',
            'img': '铭牌照片',
        }
        widgets = {
            'img': forms.widgets.FileInput()
        }
        error_messages = {
            'serial_number': {
                'unique': '此序列号已经存在!',
            },
            'mac_addr': {
                'required': '若暂时不知道MAC，请填写FFFF-FFFF-FFFF',
            }
        }

    def clean_mac_addr(self):
        """
        检查mac地址的合法性
        :return:
        """
        mac_addr = self.cleaned_data.get('mac_addr')
        # valid = re.compile(r'''
        #                     (^([0-9A-F]{1,2}[-]){5}([0-9A-f]{1,2})$
        #                     |^([0-9A-F]{1,2}[:]){5}([0-9A-f]{1,2})$
        #                     |^([0-9A-F]{1,2}[.]){5}([0-9A-f]{1,2})$)
        #                     ''',
        #                    re.VERBOSE | re.IGNORECASE)
        valid = re.compile(r'''
                            (^([0-9A-F]{4}[-])([0-9A-f]{4}[-])([0-9A-F]{4})$)
                            ''',
                           re.VERBOSE | re.IGNORECASE)
        if not valid.match(mac_addr):
            raise ValidationError('注意MAC地址的格式XXXX-XXXX-XXXX')
        return mac_addr

    def clean_img(self):
        """
        如果没有上传图片，则添加默认
        :return:
        """
        # print("cleaned_data", self.cleaned_data.get('img'))
        if not self.cleaned_data.get('img'):
            return 'computer/none.jpg'
        return self.cleaned_data.get('img')


class UserModelForm(BootStrapModelForm):
    class Meta:
        fields = "__all__"
        # exclude = ['status']
        model = models.User


class DepModelForm(BootStrapModelForm):
    class Meta:
        fields = "__all__"
        model = models.Department

        labels = {
            'departname': '科室',
        }
        error_messages = {
            'departname': {'required': '科室不能为空！',
                           'unique': '有重名的科室'}
        }


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


class AdminModelForm(BootStrapModelForm):
    """
    新建管理员
    """
    confirm_password = forms.CharField(max_length=32,
                                       label='确认密码',
                                       widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_username(self):
        # 检查管理员是否已经存在
        username_txt = self.cleaned_data.get('username')
        # 查询数据库中是否存在此管理员
        if models.Admin.objects.filter(username=username_txt).first():
            raise ValidationError("此管理员已经存在!")
        return username_txt

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))

        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库中就是什么
        return confirm


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(max_length=32,
                                       label='确认密码',
                                       widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和输入的密码是否一致
        if models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists():
            raise ValidationError("不能和以前的密码相同")

        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))

        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库中就是什么
        return confirm
