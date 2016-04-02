# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('premio', models.CharField(max_length=100)),
                ('aquisicoes', models.IntegerField()),
                ('estabelecimento', models.ForeignKey(to='estabelecimento.Estabelecimento')),
            ],
        ),
    ]
