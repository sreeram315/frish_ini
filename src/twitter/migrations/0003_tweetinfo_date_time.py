# Generated by Django 2.1.3 on 2018-12-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20181208_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetinfo',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
