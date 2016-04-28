# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0008_auto_20160426_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zawodnik',
            name='nr_zawodnika',
            field=models.IntegerField(),
        ),
    ]
