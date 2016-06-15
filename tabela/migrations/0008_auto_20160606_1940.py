# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0007_auto_20160529_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=50)),
                ('data_powstania', models.DateField()),
                ('punkty', models.IntegerField(null=True)),
                ('porazki', models.IntegerField(null=True)),
                ('zwyciestwa', models.IntegerField(null=True)),
                ('remisy', models.IntegerField(null=True)),
                ('image', models.FileField(null=True, upload_to=b'', blank=True)),
                ('stadion', models.ForeignKey(to='tabela.Stadion')),
                ('trener', models.ForeignKey(to='tabela.Trener')),
            ],
        ),
        migrations.RemoveField(
            model_name='cost',
            name='project',
        ),
        migrations.RemoveField(
            model_name='project',
            name='manager',
        ),
        migrations.DeleteModel(
            name='Cost',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
