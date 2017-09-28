# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cleaningdetails', '0006_auto_20170928_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='dhansiri_authorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webmail_id', models.EmailField(max_length=254)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaningdetails.designations')),
            ],
        ),
        migrations.CreateModel(
            name='dibang_authorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webmail_id', models.EmailField(max_length=254)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaningdetails.designations')),
            ],
        ),
        migrations.CreateModel(
            name='dihing_authorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webmail_id', models.EmailField(max_length=254)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaningdetails.designations')),
            ],
        ),
        migrations.CreateModel(
            name='kapili_authorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webmail_id', models.EmailField(max_length=254)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaningdetails.designations')),
            ],
        ),
        migrations.CreateModel(
            name='lohit_authorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webmail_id', models.EmailField(max_length=254)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaningdetails.designations')),
            ],
        ),
        migrations.CreateModel(
            name='manas_authorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webmail_id', models.EmailField(max_length=254)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaningdetails.designations')),
            ],
        ),
        migrations.CreateModel(
            name='siang_authorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webmail_id', models.EmailField(max_length=254)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaningdetails.designations')),
            ],
        ),
        migrations.CreateModel(
            name='subansiri_authorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('webmail_id', models.EmailField(max_length=254)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cleaningdetails.designations')),
            ],
        ),
    ]