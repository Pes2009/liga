# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nazwa', models.CharField(unique=True, max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('punkty', models.IntegerField(null=True)),
                ('porazki', models.IntegerField(null=True)),
                ('zwyciestwa', models.IntegerField(null=True)),
                ('remisy', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trener',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('data_urodzenia', models.DateField()),
                ('klub', models.ForeignKey(to='tabela.Klub')),
            ],
        ),
        migrations.CreateModel(
            name='Zawodnik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr_zawodnika', models.IntegerField(unique=True)),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('pozycja', models.CharField(max_length=50, null=True)),
                ('data_urodzenia', models.DateField()),
                ('klub', models.ForeignKey(to='tabela.Klub')),
            ],
        ),
    ]
