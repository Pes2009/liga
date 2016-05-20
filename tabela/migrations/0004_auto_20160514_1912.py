# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0003_auto_20160514_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_mecz',
            name='stadion_nr',
            field=models.ForeignKey(to='tabela.Stadion'),
        ),
    ]
