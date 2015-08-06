# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HmmerDB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(help_text=b'Scientific or common name', unique=True, max_length=202)),
            ],
        ),
        migrations.CreateModel(
            name='HmmerQueryRecord',
            fields=[
                ('task_id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('enqueue_date', models.DateTimeField(auto_now_add=True)),
                ('dequeue_date', models.DateTimeField(null=True)),
                ('result_date', models.DateTimeField(null=True)),
                ('result_status', models.CharField(default=b'WAITING', max_length=32)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
