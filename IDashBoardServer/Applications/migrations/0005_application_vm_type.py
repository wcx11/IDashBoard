# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0004_auto_20150503_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='vm_type',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
