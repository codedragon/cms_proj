# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('posts', models.ManyToManyField(blank=True, related_name='categories', to='cmsblog.Post')),
            ],
        ),
    ]
