# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0007_auto_20160426_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='klub',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='klub',
            name='Nazwa',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
