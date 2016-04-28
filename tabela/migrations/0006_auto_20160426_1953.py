# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0005_auto_20160426_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='strzelcy',
            name='kasysty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='strzelcy',
            name='gole_zawodnika',
            field=models.ForeignKey(to='tabela.Info_mecz'),
        ),
    ]
