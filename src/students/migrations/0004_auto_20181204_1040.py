# Generated by Django 2.1.3 on 2018-12-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20181203_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
