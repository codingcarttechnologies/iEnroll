# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 11:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ACME_Rosacea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_date', models.DateField()),
                ('site', models.CharField(choices=[(b'FV', b'Fuquay-Varina'), (b'Bahama', b'Bahama'), (b'Mills', b'Mills River')], default=b'FV', max_length=25)),
                ('lead_type', models.CharField(blank=True, choices=[(b'call', b'Call'), (b'webform', b'WebForm')], max_length=10, null=True)),
                ('fname', models.CharField(max_length=10, verbose_name=b'Contact First Name')),
                ('lname', models.CharField(max_length=15, verbose_name=b'Contact Last Name')),
                ('mi', models.CharField(blank=True, max_length=1, null=True, verbose_name=b'Contact Middle Initial')),
                ('phone1', models.CharField(max_length=15, verbose_name=b'Phone1')),
                ('phone2', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'Phone2')),
                ('contact_email', models.EmailField(max_length=254)),
                ('time_to_reach', models.DurationField(blank=True, null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=25, null=True)),
                ('near_clinic', models.NullBooleanField(default=False)),
                ('pregnant', models.NullBooleanField(default=False)),
                ('facial_hair', models.NullBooleanField(default=False)),
                ('stop_rx', models.NullBooleanField(default=False, verbose_name=b'Willing to stop Rx')),
                ('contact_att1', models.CharField(choices=[(b'successful', b'Successful'), (b'message', b'Message'), (b'no_answer', b'No Answer')], max_length=15)),
                ('contact_att2', models.CharField(choices=[(b'successful', b'Successful'), (b'message', b'Message'), (b'no_answer', b'No Answer')], max_length=15)),
                ('status', models.CharField(choices=[(b'pending', b'Pending'), (b'screened_ienroll', b'Screened by iEnroll'), (b'fail_ienroll', b'Failed iEnroll Screen'), (b'fail_client', b'Fail Client Screen'), (b'too_far', b'Not Interested, Too Far'), (b'placebo', b'Not Intereseted, Placebo'), (b'enrolled', b'Enrolled')], default=b'pending', max_length=15)),
                ('accepted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ACME_Rosacea',
            },
        ),
        migrations.CreateModel(
            name='ACME_T2D',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(blank=True, choices=[(b'Charlotte', b'Charlotte'), (b'Raleigh', b'Raleigh'), (b'WS', b'Winston-Salem')], default=b'Charlotte', max_length=25)),
                ('contact_date', models.DateField()),
                ('lead_type', models.CharField(blank=True, choices=[(b'call', b'Call'), (b'webform', b'WebForm')], max_length=10, null=True)),
                ('fname', models.CharField(max_length=10, verbose_name=b'Contact First Name')),
                ('lname', models.CharField(max_length=15, verbose_name=b'Contact Last Name')),
                ('mi', models.CharField(blank=True, max_length=1, null=True, verbose_name=b'Contact Middle Initial')),
                ('phone1', models.CharField(max_length=15, verbose_name=b'Phone1')),
                ('phone2', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'Phone2')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('time_to_reach', models.CharField(blank=True, choices=[(b'any', b'Any'), (b'morning', b'Morning'), (b'noon', b'Noon'), (b'afternoon', b'Afternoon'), (b'evening', b'Evening')], default=b'afternoon', max_length=50, null=True)),
                ('near_clinic', models.NullBooleanField(default=False)),
                ('diagnosis', models.CharField(blank=True, max_length=25, null=True)),
                ('height', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Height (inches)')),
                ('weight', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'Weight (pounds)')),
                ('triglycerides', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('lipids', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('pulse', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('bp', models.CharField(blank=True, max_length=7, null=True)),
                ('notes', models.TextField(blank=True, max_length=512, null=True)),
                ('reviewed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[(b'pending_customer', b'Pending Customer Review'), (b'screened_ienroll', b'Screened by iEnroll'), (b'fail_ienroll', b'Failed iEnroll Screen'), (b'fail_client', b'Fail Client Screen'), (b'too_far', b'Not Interested, Too Far'), (b'placebo', b'Not Intereseted, Placebo'), (b'enrolled', b'Enrolled')], default=b'pending', max_length=25)),
                ('accepted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ACME_T2D',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming'), (b'PR', b'Puerto Rico'), (b'VI', b'U.S. Virgin Islands')], max_length=2)),
                ('contact_fname', models.CharField(max_length=10, verbose_name=b'Contact First Name')),
                ('contact_lname', models.CharField(max_length=15, verbose_name=b'Contact Last Name')),
                ('contact_mi', models.CharField(blank=True, max_length=1, null=True, verbose_name=b'Contact Middle Initial')),
                ('contact_ph1', models.CharField(max_length=15, verbose_name=b'Phone1')),
                ('contact_ph2', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'Phone2')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='StarFleet_Di_Li',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(choices=[(b'Earth', b'Earth'), (b'Vulcan', b'Vulcan'), (b'Kronos', b'Kronos'), (b'other', b'Other')], default=b'Earth', max_length=25)),
                ('contact_date', models.DateField()),
                ('lead_type', models.CharField(blank=True, choices=[(b'call', b'Call'), (b'webform', b'WebForm')], max_length=10, null=True)),
                ('fname', models.CharField(max_length=10, verbose_name=b'Contact First Name')),
                ('lname', models.CharField(max_length=15, verbose_name=b'Contact Last Name')),
                ('mi', models.CharField(blank=True, max_length=1, null=True, verbose_name=b'Contact Middle Initial')),
                ('phone1', models.CharField(max_length=15, verbose_name=b'Phone1')),
                ('phone2', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'Phone2')),
                ('contact_email', models.EmailField(max_length=254)),
                ('time_to_reach', models.DurationField(blank=True, null=True)),
                ('years_in_space', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('work_in_engineeriing', models.BooleanField(default=False)),
                ('exposed_to_di_li', models.BooleanField(default=False)),
                ('contact_att1', models.CharField(choices=[(b'successful', b'Successful'), (b'message', b'Message'), (b'no_answer', b'No Answer')], max_length=15)),
                ('contact_att2', models.CharField(choices=[(b'successful', b'Successful'), (b'message', b'Message'), (b'no_answer', b'No Answer')], max_length=15)),
                ('status', models.CharField(choices=[(b'pending', b'Pending'), (b'screened_ienroll', b'Screened by iEnroll'), (b'fail_ienroll', b'Failed iEnroll Screen'), (b'fail_client', b'Fail Client Screen'), (b'too_far', b'Not Interested, Too Far'), (b'placebo', b'Not Intereseted, Placebo'), (b'enrolled', b'Enrolled')], default=b'pending', max_length=15)),
                ('accepted', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Customer')),
            ],
            options={
                'verbose_name': 'StarFleet_Di_Li',
            },
        ),
        migrations.CreateModel(
            name='Trials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('contract_id', models.CharField(max_length=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('acceptance_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Customer')),
            ],
            options={
                'verbose_name': 'Trial',
                'verbose_name_plural': 'Trials',
            },
        ),
        migrations.AddField(
            model_name='acme_t2d',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Customer'),
        ),
        migrations.AddField(
            model_name='acme_rosacea',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Customer'),
        ),
    ]
