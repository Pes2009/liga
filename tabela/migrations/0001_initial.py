# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            ],
        ),
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nazwa', models.CharField(unique=True, max_length=50)),
                ('data_powstania', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('punkty', models.IntegerField(null=True)),
                ('porazki', models.IntegerField(null=True)),
                ('zwyciestwa', models.IntegerField(null=True)),
                ('remisy', models.IntegerField(null=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.FileField(null=True, upload_to=b'', blank=True)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
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
                ('nr_zawodnika', models.IntegerField()),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('pozycja', models.CharField(max_length=50, null=True)),
                ('data_urodzenia', models.DateField()),
                ('klub', models.ForeignKey(to='tabela.Klub')),
            ],
        ),
        migrations.AddField(
            model_name='info_mecz',
            name='nr_meczu',
            field=models.ForeignKey(to='tabela.Mecz'),
        ),
        migrations.AddField(
            model_name='info_mecz',
            name='nr_zawodnika',
            field=models.ForeignKey(to='tabela.Zawodnik'),
        ),
    ]
