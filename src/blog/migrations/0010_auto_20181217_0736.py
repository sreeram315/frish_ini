# Generated by Django 2.1.3 on 2018-12-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_bloginfo_use_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloginfo',
            name='preview_points',
            field=models.TextField(blank=True, null=True),
        ),
    ]
