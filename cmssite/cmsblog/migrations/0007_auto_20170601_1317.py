# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsblog', '0006_auto_20170528_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='speaker',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cmsblog.Speaker'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='contact_email',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='venue',
            name='contact_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='venue',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
