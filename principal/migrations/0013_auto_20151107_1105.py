# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0012_auto_20151107_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='imagen_instrumento',
            field=models.ImageField(verbose_name='Imagen', null=True, blank=True, upload_to='images/'),
        ),
    ]
