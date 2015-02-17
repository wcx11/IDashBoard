# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoardUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboarduser',
            name='department',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dashboarduser',
            name='phone',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
