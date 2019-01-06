# Generated by Django 2.1.3 on 2018-12-14 09:52

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181214_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloginfo',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=blog.models.get_location, width_field='width_field'),
        ),
    ]
