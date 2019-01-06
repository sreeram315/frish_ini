# Generated by Django 2.1.3 on 2018-12-11 16:44

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_studentinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='cgpa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='department',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='section',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[students.validators.validate_section]),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
