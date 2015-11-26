# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_neighbor_app', '0003_auto_20151126_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='start_live',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(verbose_name=b'date of creation'),
        ),
    ]
