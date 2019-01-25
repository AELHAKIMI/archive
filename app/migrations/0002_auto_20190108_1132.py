# Generated by Django 2.1 on 2019-01-08 10:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='index_patient',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999)], verbose_name='Index Patient'),
        ),
    ]
