from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.models import LogEntry

from typeidea.custom_site import custom_site


class BaseOwnerAdmin(admin.ModelAdmin):

    exclude = ('owner',)


    #使列表仅显示当前用户的数据
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


    # 设置当前用户对象
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

@admin.register(LogEntry,site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user', 'change_message')


