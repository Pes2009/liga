# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0002_actor_director_genre_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecz',
            name='stadion_nr',
            field=models.ForeignKey(to='tabela.Stadion'),
        ),
    ]
