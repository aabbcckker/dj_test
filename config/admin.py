from django.contrib import admin
from .models import Link, Sidebar
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.

@admin.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')



@admin.register(Sidebar)
class SidebarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'type', 'content', 'created_time')
    fields = ('title', 'type', 'content')


