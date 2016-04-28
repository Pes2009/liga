# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0006_auto_20160426_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strzelcy',
            name='gole_zawodnika',
        ),
        migrations.RemoveField(
            model_name='strzelcy',
            name='nr_zawodnika',
        ),
        migrations.RemoveField(
            model_name='klub',
            name='id',
        ),
        migrations.AlterField(
            model_name='klub',
            name='Nazwa',
            field=models.CharField(max_length=50, unique=True, serialize=False, primary_key=True),
        ),
        migrations.DeleteModel(
            name='Strzelcy',
        ),
    ]
