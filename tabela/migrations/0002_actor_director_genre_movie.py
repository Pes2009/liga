# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40, verbose_name='Imi\u0119')),
                ('last_name', models.CharField(max_length=40, verbose_name='Nazwisko')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40, verbose_name='Imi\u0119')),
                ('last_name', models.CharField(max_length=40, verbose_name='Nazwisko')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='tytu\u0142')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Tytu\u0142')),
                ('rating', models.PositiveIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')])),
                ('actors', models.ManyToManyField(to='tabela.Actor', blank=True)),
                ('directors', models.ManyToManyField(to='tabela.Director', blank=True)),
                ('genres', models.ManyToManyField(to='tabela.Genre', blank=True)),
            ],
        ),
    ]
