# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-15 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='UNK', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='UNK', max_length=20),
        ),
        migrations.AddField(
            model_name='interest',
            name='fdr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='credit',
            name='cash_reserve',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='credit',
            name='existing_npa',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='interest',
            name='mclr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
