# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Applications', '0002_application_pvm'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='submissionTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 15, 57, 39, 775074, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
