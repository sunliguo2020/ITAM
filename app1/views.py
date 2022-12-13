from django.shortcuts import render, redirect
from . import models
from app1.utils.form import ComputerModelForm,UserModelForm,DepModelForm


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