# Generated by Django 2.1.3 on 2018-12-15 13:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20181215_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentsinfo',
            name='likes',
        ),
        migrations.AddField(
            model_name='commentsinfo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liking', to=settings.AUTH_USER_MODEL),
        ),
    ]