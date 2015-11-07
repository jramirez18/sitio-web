# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
