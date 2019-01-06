# Generated by Django 2.1.3 on 2018-12-20 05:16

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20181216_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='section',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[students.validators.validate_section]),
        ),
    ]
