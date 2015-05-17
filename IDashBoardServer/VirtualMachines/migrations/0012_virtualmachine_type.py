# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0011_auto_20150503_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='type',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
