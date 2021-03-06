# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-31 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_acme_t2d_tracking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acme_t2d',
            name='status',
            field=models.CharField(choices=[(b'pending_customer', b'Pending Customer Review'), (b'screened_ienroll', b'Screened by iEnroll'), (b'fail_ienroll', b'Failed iEnroll Screen'), (b'fail_client', b'Fail Client Screen'), (b'too_far', b'Not Interested, Too Far'), (b'placebo', b'Not Intereseted, Placebo'), (b'enrolled', b'Enrolled')], default=b'pending_customer', max_length=25),
        ),
    ]
