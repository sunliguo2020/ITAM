# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/16 8:46
"""
from django.shortcuts import render, redirect
from app1 import models
from app1.utils.form import AdminModelForm,AdminResetModelForm


def admin_list(request):
    queryset = models.Admin.objects.all()
    context = {
        'queryset': queryset
    }

    return render(request, 'admin_list.html', context)


def admin_add(request):
    title = "添加管理员"
    if request.method == 'GET':
        form = AdminModelForm()
        context = {
            'form': form,
            'title': title
        }
        return render(request, 'add.html', context)
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'add.html', context)


def admin_delete(request, nid):
    cur_user_id = request.session.get('info').get('id')
    if nid != cur_user_id:
        models.Admin.objects.filter(id=nid).delete()
        return redirect("/admin/list")
    else:
        return render(request, 'error.html', {"error_msg": "不能删除当前用户"})


def admin_reset(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {"error_msg": "此管理员不存在!"})
    title = f"重置密码：{row_object.username}"
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'change.html', {"title": title, "form": form})
    form = AdminResetModelForm(instance=row_object, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/admin/list")
    return render(request, 'change.html', {"title": title, "form": form})
