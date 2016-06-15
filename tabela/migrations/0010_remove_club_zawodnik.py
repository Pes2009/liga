# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0009_auto_20160606_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='zawodnik',
        ),
    ]
