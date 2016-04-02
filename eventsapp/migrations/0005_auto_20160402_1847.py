# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0004_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='users',
        ),
        migrations.AddField(
            model_name='club',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
