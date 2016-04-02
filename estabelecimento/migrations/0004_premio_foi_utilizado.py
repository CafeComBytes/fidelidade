# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0003_auto_20160402_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='premio',
            name='foi_utilizado',
            field=models.BooleanField(default=False),
        ),
    ]
