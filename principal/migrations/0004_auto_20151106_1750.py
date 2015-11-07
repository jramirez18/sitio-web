# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_instrumento_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='imagen',
        ),
        migrations.AddField(
            model_name='instrumento',
            name='imagen_instrumento',
            field=models.ImageField(verbose_name='Imagen', upload_to='images/', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(verbose_name='Nombre categoria', max_length=100),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='fecha_creacion',
            field=models.DateTimeField(verbose_name='Fecha de creacion', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='fecha_publicacion',
            field=models.DateTimeField(verbose_name='Fecha de publicacion', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='marca',
            field=models.CharField(verbose_name='Marca', max_length=100),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='nombre',
            field=models.CharField(verbose_name='Nombre', max_length=100),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='precio',
            field=models.DecimalField(verbose_name='Precio', max_digits=8, decimal_places=2),
        ),
    ]
