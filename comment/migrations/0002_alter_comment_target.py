# Generated by Django 4.1 on 2024-04-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="target",
            field=models.CharField(max_length=100, verbose_name="评论目标"),
        ),
    ]
