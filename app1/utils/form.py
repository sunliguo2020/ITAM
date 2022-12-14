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
from .bootstrap import BootStrapModelForm


class ComputerModelForm(BootStrapModelForm):
    class Meta:
        fields = "__all__"
        model = models.Computer
        error_messages = {
            'serial_number': {
                'unique': '此序列号已经存在!',
            },
            'mac_addr': {
                'required': '若暂时不知道MAC，请填写FFFF-FFFF-FFFF'
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
