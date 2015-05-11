# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0008_auto_20150406_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='parent',
            field=models.ForeignKey(related_name='p', to='VirtualMachines.VirtualMachine', null=True),
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='uuid',
            field=models.TextField(null=True),
        ),
    ]
