# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(verbose_name='代码', max_length=10)),
                ('name', models.CharField(verbose_name='简称', max_length=10)),
                ('induestry', models.CharField(verbose_name='行业', max_length=20)),
                ('year', models.CharField(verbose_name='年份', max_length=5)),
                ('content', models.TextField(verbose_name='年报内容', blank=True, null=True)),
            ],
        ),
    ]
