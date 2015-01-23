# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0002_delete_virtualmachine'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualMachine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IPAddress', models.IPAddressField()),
                ('port', models.PositiveIntegerField(null=True)),
                ('state', models.IntegerField(null=True)),
                ('lastConnectTime', models.DateTimeField(auto_now=True)),
                ('stateInfo', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
