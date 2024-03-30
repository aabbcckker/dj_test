# Generated by Django 4.1 on 2024-03-29 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Sidebar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="标题")),
                (
                    "type",
                    models.IntegerField(
                        choices=[(1, "HTML"), (2, "最新文章"), (3, "最热文章"), (4, "最近评论")],
                        default=1,
                        verbose_name="展示形势",
                    ),
                ),
                (
                    "status",
                    models.PositiveIntegerField(
                        choices=[(1, "展示"), (0, "隐藏")], default=1, verbose_name="状态"
                    ),
                ),
                (
                    "content",
                    models.CharField(blank=True, max_length=500, verbose_name="内容"),
                ),
                (
                    "created_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
            options={
                "verbose_name": ("侧边栏",),
                "verbose_name_plural": ("侧边栏",),
            },
        ),
        migrations.CreateModel(
            name="Link",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="标题")),
                ("href", models.URLField(verbose_name="链接")),
                (
                    "status",
                    models.PositiveIntegerField(
                        choices=[(1, "正常"), (0, "删除")], default=1, verbose_name="状态"
                    ),
                ),
                (
                    "created_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "weight",
                    models.PositiveIntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        default=1,
                        verbose_name="权重",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="作者",
                    ),
                ),
            ],
            options={
                "verbose_name": "友链",
                "verbose_name_plural": "友链",
            },
        ),
    ]
