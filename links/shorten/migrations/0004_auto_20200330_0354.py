# Generated by Django 3.0.3 on 2020-03-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0003_auto_20200329_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urltable',
            name='no_clicks',
            field=models.IntegerField(null=True),
        ),
    ]