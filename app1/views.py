from django.shortcuts import render, redirect
from . import models
from app1.utils.form import ComputerModelForm, UserModelForm, DepModelForm


# Create your views here.
def computer_list(request):
    queryset = models.Computer.objects.all()
    context = {
        "queryset": queryset
    }
    return render(request, 'computer_list.html', context)


def computer_add(request):
    """
    电脑添加页面
    :param request:
    :return:
    """
    if request.method == "GET":
        form = ComputerModelForm()
        context = {
            "form": form
        }
        return render(request, 'computer_add.html', context)
    form = ComputerModelForm(request.POST)
    if form.is_valid():
        form.save()

        return redirect('/computer/list/')
    return render(request, 'computer_add.html', {'form': form})


def computer_edit(request, nid):
    """电脑编辑"""
    title = '电脑编辑'
    row_obj = models.Computer.objects.filter(id=nid).first()

    if request.method == "GET":
        form = ComputerModelForm(instance=row_obj)
        context = {
            'form': form,
            'title': title
        }
        return render(request, 'change.html', context)
    form = ComputerModelForm(request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/computer/list/')
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'change.html', context)


def computer_delete(request, nid):
    """电脑删除"""
    models.Computer.objects.filter(id=nid).delete()

    return redirect('/computer/list/')


def user_list(request):
    queryset = models.User.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'user_list.html', context)


def user_add(request):
    """
    用户添加页面
    :param request:
    :return:
    """
    if request.method == "GET":
        form = UserModelForm()
        context = {
            "form": form
        }
        return render(request, 'user_add.html', context)
    form = UserModelForm(request.POST)
    if form.is_valid():
        form.save()

        return redirect('/user/list/')
    return render(request, 'user_add.html', {'form': form})


def user_edit(request, nid):
    # row_obj = models.User.objects.filter(id=nid).first()
    row_obj = models.User.objects.get(id=nid)
    if request.method =="GET":

        form = UserModelForm(instance=row_obj)
        context = {
            'form': form
        }
        return render(request, 'change.html', context)
    form = UserModelForm(data=request.POST,instance = row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')

    context = {
        "form":form
    }
    return render(request, 'change.html', context)

def dep_list(request):
    queryset = models.Department.objects.all()
    context = {
        'queryset': queryset
    }

    return render(request, 'dep_list.html', context)


def dep_add(request):
    """
     部门添加页面
     :param request:
     :return:
     """
    if request.method == "GET":
        form = DepModelForm()
        context = {
            "form": form
        }
        return render(request, 'dep_add.html', context)
    form = DepModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/dep/list/')
    return render(request, 'dep_add.html', {'form': form})


def user_delete(request,nid):
    models.User.objects.filter(id=nid).delete()

    return redirect('/user/list/')


def dep_delete(request,nid):
    models.Department.objects.filter(id=nid).delete()
    return redirect('/dep/list/')


def dep_edit(request,nid):
    row_obj = models.Department.objects.filter(id=nid).first()
    if request.method == "GET":

        form = DepModelForm(instance = row_obj)
        context ={
            "form":form
        }
        return render(request,'change.html',context)

    form = DepModelForm(data = request.POST,instance = row_obj)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()

        return redirect('/dep/list/')
    return render(request,'change.html',context)