# Generated by Django 2.1.3 on 2018-12-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20181204_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
