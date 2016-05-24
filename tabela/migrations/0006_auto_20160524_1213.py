# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0005_auto_20160520_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='directors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
