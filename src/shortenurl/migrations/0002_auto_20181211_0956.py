# Generated by Django 2.1.3 on 2018-12-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenurl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlinfo',
            name='original_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
