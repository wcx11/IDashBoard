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
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField()),
                ('OS', models.IntegerField()),
                ('HostName', models.TextField()),
                ('UserName', models.TextField()),
                ('Memory', models.IntegerField()),
                ('state', models.IntegerField()),
                ('applicant', models.ForeignKey(related_name='applicant', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(related_name='reviewer', to=settings.AUTH_USER_MODEL, null=True)),
                ('vm', models.ForeignKey(related_name='vm', to='VirtualMachines.VirtualMachine', null=True)),
            ],
        ),
    ]
