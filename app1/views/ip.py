# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-16 18:32
"""
from django.shortcuts import render, redirect
from app1 import models
from app1.utils.form import IpModelForm


def ip_list(request):
    queryset = models.IpAddr.objects.all()
    context = {
        'queryset': queryset,
    }
    return render(request, 'ip_list.html', context)


def ip_add(request):
    if request.method == 'GET':
        title = '新增Ip地址'
        form = IpModelForm()
        context = {
            'form': form
        }
        return render(request, 'add.html', context)
    form = IpModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/ip/list/')
    context = {
        'form': form
    }
    return render(request, 'add.html', context)


def ip_edit(request, nid):
    obj = models.IpAddr.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = IpModelForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'change.html', context)
    form = IpModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/ip/list/')
    context = {
        'form': form
    }
    return render(request, 'change.html', context)


def ip_delete(request,nid):
    models.IpAddr.objects.filter(id=nid).delete()
    return redirect('/ip/list/')