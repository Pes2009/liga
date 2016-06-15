# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0008_auto_20160606_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='barwy',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='przydomek',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='strona',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='zawodnik',
            field=models.ForeignKey(default=10, to='tabela.Zawodnik'),
            preserve_default=False,
        ),
    ]
