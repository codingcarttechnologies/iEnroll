# forms.py
#
# David R. McWilliams <dave@ienrolldigital.com>
# 13-Feb-2017 Initiate

from django.forms import ModelForm
from contacts.models import ACME_T2D

class ACME_T2D_ContactForm(ModelForm):
    '''Input form for the ACME_T2D trial'''

    class Meta:
        model = ACME_T2D
        fields = ['contact_date', 'lead_type', 'site', 'fname', 'lname', 'mi', 'phone1',
                  'phone2', 'contact_email', 'time_to_reach', 'near_clinic', 'diagnosis',
                  'height', 'weight', 'triglycerides', 'lipids', 'pulse', 'bp', 'notes',
                  'reviewed', 'status', 'accepted',]
