# Generated by Django 4.1 on 2024-03-31 02:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("config", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sidebar",
            options={"verbose_name": "侧边栏", "verbose_name_plural": "侧边栏"},
        ),
    ]