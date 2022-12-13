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


class UserModelForm(BootStrapModelForm):
    class Meta:
        fields = "__all__"
        model = models.User


class DepModelForm(BootStrapModelForm):
    class Meta:
        fields = "__all__"
        model = models.Department
