# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_remove_recurso_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='es_favorito',
            field=models.IntegerField(),
        ),
    ]