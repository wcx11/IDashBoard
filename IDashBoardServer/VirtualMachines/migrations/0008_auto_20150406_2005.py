# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0007_virtualmachine_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualmachine',
            name='IPAddress',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
