# Generated by Django 2.1.3 on 2018-12-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20181204_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='description',
            field=models.CharField(blank=True, max_length=9999, null=True),
        ),
    ]
