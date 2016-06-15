# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0011_auto_20160609_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=50)),
                ('data_powstania', models.DateField()),
                ('punkty', models.IntegerField(null=True)),
                ('porazki', models.IntegerField(null=True)),
                ('zwyciestwa', models.IntegerField(null=True)),
                ('remisy', models.IntegerField(null=True)),
                ('image', models.FileField(null=True, upload_to=b'', blank=True)),
                ('barwy', models.CharField(max_length=50)),
                ('przydomek', models.CharField(max_length=50)),
                ('strona', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='stadion',
            name='klubs',
            field=models.ForeignKey(to='tabela.Clubs'),
        ),
        migrations.AlterField(
            model_name='trener',
            name='klubs',
            field=models.ForeignKey(to='tabela.Clubs'),
        ),
        migrations.AlterField(
            model_name='zawodnik',
            name='klubs',
            field=models.ForeignKey(to='tabela.Clubs'),
        ),
        migrations.DeleteModel(
            name='Club',
        ),
    ]
