# Generated by Django 2.1 on 2019-12-24 16:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0004_auto_20191225_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]