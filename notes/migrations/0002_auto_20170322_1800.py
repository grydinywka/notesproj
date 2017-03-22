# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 18:00
from __future__ import unicode_literals

from django.db import migrations

def load_notes_users_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "initial_data.json")


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_notes_users_from_fixture),
    ]
