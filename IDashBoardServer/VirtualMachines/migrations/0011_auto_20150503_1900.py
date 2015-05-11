# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualMachines', '0010_auto_20150428_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='vmHost',
            field=models.ForeignKey(related_name='vm_host', to='VirtualMachines.VirtualMachine', null=True),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='IPAddress',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='vmUser',
            field=models.ForeignKey(related_name='vm_user', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
