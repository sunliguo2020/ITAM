# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/13 11:54
"""

from django import forms
from app1 import models
from .bootstrap import BootStrapModelForm


class ComputerModelForm(BootStrapModelForm):
    class Meta:
        fields = "__all__"
        model = models.Computer
        error_messages = {
            'serial_number': {
                'unique': '此序列号已经存在!',
            }
        }


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
