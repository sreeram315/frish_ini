# Generated by Django 2.1.3 on 2018-12-06 18:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinfo',
            name='owner',
            field=models.OneToOneField(on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
