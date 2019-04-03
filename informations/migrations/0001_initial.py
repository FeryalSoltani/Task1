# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=150)),
                ('UserID', models.IntegerField(max_length=10)),
                ('PhoneNum', models.IntegerField(max_length=20)),
                ('Email', models.CharField(max_length=150)),
                ('Purchase', models.CharField(max_length=150)),
                ('PurchaseID', models.IntegerField()),
                ('DateTime', models.DateField()),
                ('Address', models.TextField()),
            ],
        ),
    ]
