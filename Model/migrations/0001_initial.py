# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onwer',
            fields=[
                ('ownerID', models.IntegerField(db_column='FId', primary_key=True, serialize=False)),
                ('ownerName', models.CharField(max_length=20)),
                ('ownerLicense', models.CharField(max_length=50)),
                ('ownerPicture', models.ImageField(upload_to='img')),
                ('ownerPassword', models.CharField(max_length=20)),
                ('ownerEmail', models.EmailField(max_length=30)),
                ('remark', models.CharField(max_length=30)),
            ],
        ),
    ]
