# Generated by Django 2.1.3 on 2018-12-07 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181207_0526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountinfo',
            name='following',
        ),
    ]
