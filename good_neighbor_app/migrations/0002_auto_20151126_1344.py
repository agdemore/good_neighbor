# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('good_neighbor_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=150, verbose_name=b'Address of place')),
                ('start_live', models.DateTimeField(default=datetime.datetime(2015, 11, 26, 13, 44, 32, 905293))),
            ],
            options={
                'verbose_name': 'Place',
            },
        ),
        migrations.AddField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 13, 44, 32, 903601), verbose_name=b'date of creation'),
        ),
        migrations.AddField(
            model_name='task',
            name='rate',
            field=models.ImageField(default=0, upload_to=b'', verbose_name=b'rate of task'),
        ),
        migrations.AddField(
            model_name='place',
            name='tasks',
            field=models.ManyToManyField(related_name='tasks', to='good_neighbor_app.Task'),
        ),
        migrations.AddField(
            model_name='place',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
