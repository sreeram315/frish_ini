# Generated by Django 2.1.3 on 2018-12-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='countinfo',
            name='creater',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='countinfo',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='countinfo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
