from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site
from .adminforms import PostAdminForm
from .models import Category,Tag,Post
# Register your models here.


# 编辑文章的标题和摘要
class Postinline(admin.TabularInline):
    fields = ('title', 'description')
    extra = 1
    model = Post

@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    #分类界面直接编辑文章的部分内容
    inlines = [Postinline]

    list_display = ('name','status','is_nav','created_time')
    fields = ['name','status','is_nav']

    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = '文章数量'

@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ['name', 'status']

#自定义过滤器
class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'  # 查询时url参数的名字

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = ('title', 'category', 'status', 'created_time', 'operater')
    list_display_links = []

    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    # filter_horizontal = ('tags',)
    # filter_horizontal = ('tags',)
    # fields = ['title', 'category', 'description', 'status', 'content', 'tags']
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),

        ('内容', {
            'fields': (
                'description',
                'content',
            ),
        }),

        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tags',),
        })
    )
    def operater(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))#!!! args中必须用可迭代对象
        )
        operator.short_description = '操作'

#     页面元素
    class Media:
        css = {
            'all': ('https://cdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css',),
        }
        js = ('https://cdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


