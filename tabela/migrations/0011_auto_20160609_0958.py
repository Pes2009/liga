# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0010_remove_club_zawodnik'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='stadion',
        ),
        migrations.RemoveField(
            model_name='club',
            name='trener',
        ),
        migrations.AddField(
            model_name='stadion',
            name='klubs',
            field=models.ForeignKey(default=1, to='tabela.Club'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trener',
            name='klubs',
            field=models.ForeignKey(default=1.1, to='tabela.Club'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zawodnik',
            name='klubs',
            field=models.ForeignKey(default=1, to='tabela.Club'),
            preserve_default=False,
        ),
    ]
