# Generated by Django 4.1 on 2024-04-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_pv_post_uv"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="comment_html",
            field=models.TextField(blank=True, editable=False, verbose_name="正文html代码"),
        ),
    ]
