# Generated by Django 2.1.3 on 2018-12-20 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagehost.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageHostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=imagehost.models.get_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
