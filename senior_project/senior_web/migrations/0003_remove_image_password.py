# Generated by Django 3.0 on 2019-12-24 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senior_web', '0002_auto_20191224_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='password',
        ),
    ]
