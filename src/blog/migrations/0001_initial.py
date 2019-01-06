# Generated by Django 2.1.3 on 2018-12-14 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('lat_updated', models.DateTimeField(auto_now=True, null=True)),
                ('age_restricted', models.BooleanField(default=False)),
                ('content', models.CharField(blank=True, max_length=50000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('genre', models.CharField(choices=[('INSPIRATIONAL', 'Inspirational'), ('EDUCATIONAL', 'Educational'), ('ENTERTAINMENT', 'Entertainment'), ('NEWS', 'News')], default='NEWS', max_length=20)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
