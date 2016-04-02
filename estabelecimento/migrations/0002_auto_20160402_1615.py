# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aquisicao',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('quem', models.CharField(max_length=11)),
                ('quando', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='promocao',
            old_name='aquisicoes',
            new_name='quantidade_necessaria',
        ),
        migrations.AddField(
            model_name='aquisicao',
            name='promocao',
            field=models.ForeignKey(to='estabelecimento.Promocao'),
        ),
    ]
