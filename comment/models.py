from django.db import models
from blog.models import Post

# Create your models here.

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_CHOICES = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    target = models.CharField(max_length=100, verbose_name='评论目标')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱')
    website = models.URLField(verbose_name='网站')
    content = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_NORMAL, verbose_name='状态')

    class Meta:
        verbose_name = verbose_name_plural = '评论'

    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(target=target, status=cls.STATUS_NORMAL)
