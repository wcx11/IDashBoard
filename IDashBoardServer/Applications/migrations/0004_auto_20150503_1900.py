# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0003_application_submissiontime'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='pwd',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='HostName',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='Memory',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='OS',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='UserName',
            field=models.TextField(null=True),
        ),
    ]
