# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0004_goals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goals',
            new_name='Strzelcy',
        ),
        migrations.AlterField(
            model_name='strzelcy',
            name='gole_zawodnika',
            field=models.ForeignKey(to='tabela.Mecz'),
        ),
    ]
