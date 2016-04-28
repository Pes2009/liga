# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0009_auto_20160427_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(unique=True, max_length=50)),
                ('miasto', models.CharField(max_length=50)),
                ('ulica', models.CharField(max_length=50)),
                ('pojemnosc', models.IntegerField()),
                ('klub', models.ForeignKey(to='tabela.Klub')),
            ],
        ),
    ]
