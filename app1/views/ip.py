# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022-12-16 18:32
"""
import csv
import os
from datetime import datetime
from pprint import pprint

import pytz
from django.shortcuts import render, redirect, HttpResponse

from app1 import models
from app1.utils.form import IpModelForm
from app1.utils.pageination import Pagination


def ip_list(request):
    """

    :param request:
    :return:
    """
    search_data = {}
    search_type = request.GET.get('search_type')
    if search_type and request.GET.get('q'):
        if search_type == 'ip_addr':
            search_data['ip_addr__icontains'] = request.GET.get('q').strip()
        elif search_type == 'mac_addr':
            search_data['mac_addr__icontains'] = request.GET.get('q').strip()

    queryset = models.IpAddr.objects.filter(**search_data)
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html()
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


def ip_delete(request, nid):
    models.IpAddr.objects.filter(id=nid).delete()
    return redirect('/ip/list/')


def ip_multi(request):
    """
    ip arp 地址对应关系导入
    :param request:
    :return:
    """
    if request.method == 'GET':
        return HttpResponse('请post上传csv文件!')
    # 是否上传空文件
    csv_File = request.FILES.get('csv_file', None)
    if not csv_File:
        return redirect('/ip/list/')
    elif os.path.splitext(csv_File.name)[1] != '.csv':
        return redirect('/ip/list/')
    path = 'media/uploads/'
    if not os.path.exists(path):
        os.makedirs(path)
    # 保存文件
    with open(os.path.join(path, csv_File.name), 'wb+') as fp:
        for chunk in csv_File.chunks():
            fp.write(chunk)
    with open(os.path.join(path, csv_File.name), encoding='utf-8') as fp:
        count = 0
        csv_read = csv.reader(fp)
        for row in csv_read:

            # 先把字符串转成不带时区的datetime
            dt = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
            # 把不带时区的datetime转成timestamp再转成秒
            ts = int(dt.timestamp())
            # 把秒转成带时区的datetime
            t = datetime.fromtimestamp(ts, pytz.timezone('Asia/Shanghai'))

            data_dict = {
                'ip_addr': row[0],
                'mac_addr': row[1],
                'interface': row[2],
                # 解决时区问题 时间字符串转为时间 datetime.strptime('2018-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
                'cap_datetime': t
                # 'cap_datetime': datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
            }

            # 方法1，先搜索，更新时间，最后save()
            # 直接搜索出数据库中时间较早的

            queryset = models.IpAddr.objects.filter(ip_addr=data_dict['ip_addr'],
                                                    mac_addr=data_dict['mac_addr'],
                                                    interface=data_dict['interface'],
                                                    cap_datetime__lte=data_dict['cap_datetime'])

            if queryset.exists():
                print('已经有数据', queryset)
                for query_row in queryset:
                    query_row.cap_datetime = data_dict['cap_datetime']
                    query_row.save()
            else:
                print('新增数据')
                models.IpAddr.objects.create(**data_dict)

            # # 方法2、直接update 有问题，烧脑筋
            # # AttributeError: 'NoneType' object has no attribute 'update'
            # result = models.IpAddr.objects.filter(ip_addr=data_dict['ip_addr'],
            #                                       mac_addr=data_dict['mac_addr'],
            #                                       interface=data_dict['interface'],
            #                                       cap_datetime__gte=data_dict['cap_datetime'])
            # # if result is not None :<class 'django.db.models.query.QuerySet'> <QuerySet []>
            # count += 1
            #
            # if result.count() > 0:
            #     # <class 'NoneType'> None
            #     print(count, ":",result.count())
            #     # 找到比 2022-04-01 04:00:02+08:00 更早或相同 2022-03-31 19:55:01+00:00
            #     print('找到比', data_dict['cap_datetime'], '更早或相同', result.first().cap_datetime)
            #
            #     result.update(cap_datetime=data_dict['cap_datetime'])
            # else:
            #     print(count, ':')
            #     pprint(data_dict)
            #     print('找不到数据,新增', type(result), result)
            #     models.IpAddr.objects.create(**data_dict)

    return redirect('/ip/list/')
