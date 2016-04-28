# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0003_info_mecz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gole_zawodnika', models.ForeignKey(to='tabela.Info_mecz')),
                ('nr_zawodnika', models.ForeignKey(to='tabela.Zawodnik')),
            ],
        ),
    ]
