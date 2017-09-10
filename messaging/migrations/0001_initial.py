# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0011_auto_20170910_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, default='')),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_recipient', to='account.UserProfile')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to='account.UserProfile')),
            ],
        ),
    ]