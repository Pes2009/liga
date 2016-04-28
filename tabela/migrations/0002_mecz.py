# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mecz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField(auto_now_add=True)),
                ('godz_spotkania', models.TimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nr_kolejki', models.IntegerField(null=True)),
                ('widownia', models.IntegerField(null=True)),
                ('czas_gry', models.TimeField(auto_now_add=True)),
                ('gole_gosci', models.IntegerField(null=True)),
                ('gole_gospodarz', models.IntegerField(null=True)),
                ('stadion_nr', models.IntegerField()),
                ('gosc', models.ForeignKey(related_name='mecz_gosc', to='tabela.Klub')),
                ('gospodarz', models.ForeignKey(related_name='mecz_gospodarz', to='tabela.Klub')),
            ],
        ),
    ]
