# Generated by Django 2.1.3 on 2018-12-14 09:48

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181214_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloginfo',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=blog.models.get_location),
        ),
    ]
