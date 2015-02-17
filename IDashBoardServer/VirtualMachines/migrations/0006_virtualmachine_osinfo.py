# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0005_auto_20150213_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='osInfo',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
