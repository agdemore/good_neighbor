# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name of category')),
                ('title', models.CharField(max_length=50, verbose_name=b'Title of category')),
            ],
            options={
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name of tag')),
                ('title', models.CharField(max_length=50, verbose_name=b'Title of tag')),
            ],
            options={
                'verbose_name': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Title of task')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(related_name='tasks', to='good_neighbor_app.Category')),
                ('tags', models.ManyToManyField(related_name='tags', to='good_neighbor_app.Tag')),
                ('user', models.ForeignKey(related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
            },
        ),
    ]
