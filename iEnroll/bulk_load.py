#!/usr/bin/env python
#
# bulk_load.py - bulk load some data.  Adapted from
# https://github.com/jadianes/winerama-recommender-tutorial/tree/stage-2.1
#
# David R. McWilliams <dave@ienrolldigital.com>
#
# 03-Mar-2017 Initiate

import sys, os
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iEnroll.settings")

import django
django.setup()

from contacts.models import ACME_T2D, Customer


def save_contact_from_row(contact_row):
    contact = ACME_T2D()

    contact.customer            = Customer.objects.get(id=contact_row[0]) # This is a foreign key
    contact.site                = contact_row[1]
    contact.contact_date        = contact_row[2]
    contact.lead_type           = contact_row[3]
    contact.fname               = contact_row[4]
    contact.lname               = contact_row[5]
    contact.mi                  = contact_row[6]
    contact.phone1              = contact_row[7]
    contact.phone2              = contact_row[8]
    contact.contact_email       = contact_row[9]
    contact.time_to_reach       = contact_row[10]
    contact.near_clinic         = contact_row[11]
    contact.diagnosis           = contact_row[12]
    contact.height              = contact_row[13]
    contact.weight              = contact_row[14]
    contact.triglycerides       = contact_row[15]
    contact.lipids              = contact_row[16]
    contact.pulse               = contact_row[17]
    contact.bp                  = contact_row[18]
    contact.status              = contact_row[19]
    contact.accepted            = contact_row[20]
    contact.notes               = contact_row[21]
    contact.reviewed            = contact_row[22]

    contact.save()

if __name__ == "__main__":

    # Check number of arguments (including the command name)
    if len(sys.argv) == 2:
        print("Reading from file " + (sys.argv[1]))
        contacts_df = pd.read_csv(sys.argv[1])

        # print(contacts_df)

        # apply save_contact_from_row to each contact in the data frame
        contacts_df.apply(
            save_contact_from_row,
            axis=1
        )

        print("There are {} contacts in DB".format(ACME_T2D.objects.count()))

    else:
        print("Please, provide contacts file path")

### End bulk_load.py
