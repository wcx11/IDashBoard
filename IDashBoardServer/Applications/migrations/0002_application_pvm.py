# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0009_auto_20150427_0745'),
        ('Applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='pvm',
            field=models.ForeignKey(related_name='pvm', to='VirtualMachines.VirtualMachine', null=True),
        ),
    ]
