# Generated by Django 3.2.7 on 2021-09-29 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0003_auto_20210929_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='classe',
        ),
    ]
