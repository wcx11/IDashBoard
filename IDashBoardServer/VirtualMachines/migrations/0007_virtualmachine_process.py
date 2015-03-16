# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0006_virtualmachine_osinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='process',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
