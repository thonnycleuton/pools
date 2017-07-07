# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-07-06 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('closed', models.BooleanField(default=False)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
