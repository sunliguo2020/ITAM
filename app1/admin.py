from django.contrib import admin

# Register your models here.
from .models import IpAddr, Computer, User, Department


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
    list_display = [
        'serial_number',
        'brand',
        'computer_type',
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
    """
    autocomplete_fields
        作用：针对多对多和一对多关系， 会将外键数据全部加载出来，渲染到select表中，如果数据量比较大，就会很慢，使用autocomplete_fields只会展示几条数据，在最上侧会出现一个搜索框，可以使用搜索框查询未显示的数据。既然有搜索，那么就需要定义搜索属性search_fields，示例如下
        
        class UserAdmin(admin.ModelAdmin):
            autocomplete_fields = ('company', )  # 外键
            
        class CompanyAdmin(admin.ModelAdmin):
            search_fields = ('title', )  # 对应的表数据能够通过某一个字段或者多个字段进行搜索
    """
    autocomplete_fields = ('owner',)  # owner 外键


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'depart', 'room_no', 'status', 'createdate', 'last_mod_time']
    search_fields = ['username', 'depart__departname']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['departname', 'createdate']
    search_fields = ['departname']
