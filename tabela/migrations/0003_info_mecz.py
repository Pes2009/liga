# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0002_mecz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info_mecz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gole_zawodnika', models.IntegerField(null=True)),
                ('zolte_kartki', models.IntegerField(null=True)),
                ('asysty', models.IntegerField(null=True)),
                ('stadion_nr', models.IntegerField()),
                ('nr_meczu', models.ForeignKey(to='tabela.Mecz')),
                ('nr_zawodnika', models.ForeignKey(to='tabela.Zawodnik')),
            ],
        ),
    ]
