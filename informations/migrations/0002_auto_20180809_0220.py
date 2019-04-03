# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='PhoneNum',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='data',
            name='UserID',
            field=models.IntegerField(),
        ),
    ]
