# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_name', models.CharField(max_length=50)),
                ('show_info', models.CharField(max_length=300)),
                ('show_type', models.IntegerField()),
                ('show_cost', models.IntegerField()),
                ('show_image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=50)),
                ('stage_info', models.CharField(max_length=300)),
                ('stage_image', models.ImageField(upload_to=b'')),
                ('stage_shows', models.ManyToManyField(to='shows.Show')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=50)),
                ('venue_info', models.CharField(max_length=300)),
                ('venue_location', models.CharField(max_length=100)),
                ('venue_stages', models.ManyToManyField(to='shows.Stage')),
            ],
        ),
    ]