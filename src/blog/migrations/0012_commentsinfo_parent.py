# Generated by Django 2.1.3 on 2018-12-20 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181217_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsinfo',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.CommentsInfo'),
        ),
    ]
