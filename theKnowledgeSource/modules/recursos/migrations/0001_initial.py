# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 00:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('lenguaje', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('PHP', 'PHP'), ('C++', 'C++'), ('javaScript', 'javaScript'), ('C#', 'C#'), ('Ruby', 'Ruby')], max_length=200)),
                ('tipo', models.CharField(choices=[('PDF', 'PDF'), ('Video', 'Video'), ('url', 'url'), ('ebook', 'ebook')], max_length=200)),
                ('nivel', models.CharField(choices=[('Básico', 'Básico'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado')], max_length=200)),
                ('es_favorito', models.BooleanField(default=True)),
                ('url', models.URLField()),
                ('archivo', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
