# Generated by Django 3.0.3 on 2020-03-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0009_auto_20200330_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urltable',
            name='no_clicks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
