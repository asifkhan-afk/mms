# Generated by Django 3.2.9 on 2022-09-14 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220914_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revenue',
            name='month',
        ),
    ]