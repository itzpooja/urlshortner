# Generated by Django 3.0.3 on 2020-03-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0004_auto_20200330_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urltable',
            name='no_clicks',
            field=models.IntegerField(),
        ),
    ]
