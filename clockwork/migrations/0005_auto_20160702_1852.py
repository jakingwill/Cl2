# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clockwork', '0004_auto_20160702_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='jobs',
        ),
        migrations.AddField(
            model_name='job',
            name='jobs',
            field=models.ManyToManyField(to='clockwork.Jobseeker'),
        ),
    ]
