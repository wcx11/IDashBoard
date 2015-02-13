# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0004_auto_20150212_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='virtualmachine',
            old_name='task',
            new_name='tasks',
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='cpuInfo',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='hostname',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='username',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
