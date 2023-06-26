from django.contrib import admin

# Register your models here.
from .models import IpAddr, Computer, User,Department


@admin.register(IpAddr)
class IpAddrAdmin(admin.ModelAdmin):
    # 设置后台列表中显示的字段
    list_display = ['id', 'ip_addr', 'mac_addr', 'interface', 'cap_datetime']
    # 搜索
    search_fields = ['ip_addr', 'mac_addr']
    # 过滤
    list_filter = ['ip_addr', 'mac_addr']
    # 设置时间选择器 Database returned an invalid datetime value. Are time zone definitions for your database installed?
    # date_hierarchy = 'cap_datetime'
    # 设置每页显示的数据量
    list_per_page = 20

    list_max_show_all = 30

    # 排序
    ordering = ['cap_datetime']


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['brand',
                    'computer_type',
                    'serial_number',
                    'owner',
                    'production_date',
                    'mac_addr',
                    'computer_img',
                    'dis_mac_img',
                    'mod_time',
                    ]
    # Related Field got invalid lookup: icontains
    search_fields = ['serial_number', 'mac_addr', 'owner__username']
    list_display_links = ['serial_number']
    list_per_page = 30


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'depart', 'status', 'createdate']
    search_fields = ['username', 'depart__departname']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['departname','createdate']
    search_fields = ['departname']
