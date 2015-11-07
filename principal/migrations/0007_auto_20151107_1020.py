# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_auto_20151107_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='imagen_instrumento',
            field=models.ImageField(verbose_name='Imagen', upload_to='/images/', blank=True, null=True),
        ),
    ]
