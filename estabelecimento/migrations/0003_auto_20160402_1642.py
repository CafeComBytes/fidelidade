# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0002_auto_20160402_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('promocao', models.ForeignKey(related_name='premios', to='estabelecimento.Promocao')),
                ('quem', models.ForeignKey(to='estabelecimento.Cliente')),
            ],
        ),
        migrations.AlterField(
            model_name='aquisicao',
            name='quem',
            field=models.ForeignKey(to='estabelecimento.Cliente'),
        ),
    ]
