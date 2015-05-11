# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('VirtualMachines', '0009_auto_20150427_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virtualmachine',
            name='parent',
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='vmUser',
            field=models.ForeignKey(related_name='vmUser', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
