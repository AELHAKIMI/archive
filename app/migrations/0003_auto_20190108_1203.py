# Generated by Django 2.1 on 2019-01-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190108_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Description'),
        ),
    ]