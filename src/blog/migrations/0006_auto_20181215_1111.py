# Generated by Django 2.1.3 on 2018-12-15 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20181214_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=5000, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commentsinfo',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogInfo'),
        ),
        migrations.AddField(
            model_name='commentsinfo',
            name='creater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]