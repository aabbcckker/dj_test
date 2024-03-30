from django.contrib import admin

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