# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 20:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useroperation', '0002_auto_20171218_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='mobile',
            new_name='signer_mobile',
        ),
    ]
