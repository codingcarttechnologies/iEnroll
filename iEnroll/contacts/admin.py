# admim.py - iEnroll website
#
# David R. McWilliams <dave@suemac.org>
# 11-Feb-2017 Initiate

from django.contrib import admin
from .models import Customer,Trials,ACME_T2D,ACME_Rosacea,StarFleet_Di_Li

# Register your models here.

admin.site.register(Customer)
admin.site.register(Trials)
# admin.site.register(ACME_T2D)
# admin.site.register(ACME_Rosacea)
# admin.site.register(StarFleet_Di_Li)

class ACME_T2D_Contacts(admin.ModelAdmin):
    fieldsets = [
        ('Call Center', {'fields': ['customer','site', 'contact_date', 'lead_type',
                                    'fname', 'lname', 'mi', 'phone1', 'phone2',
                                    'contact_email', 'time_to_reach']}),
        ('ACME', {'fields': ['near_clinic', 'diagnosis', 'height', 'weight',
                             'triglycerides', 'lipids', 'pulse', 'bp', 'notes',
                             'reviewed', 'status', 'accepted']}),
    ]

    list_display = ['fname', 'lname', 'status']
    list_filter = ['status']

admin.site.register(ACME_T2D, ACME_T2D_Contacts)

class ACME_Rosacea_Contacts(admin.ModelAdmin):
    fieldsets = [
        ('Call Center', {'fields': ['site', 'contact_date', 'lead_type',
                                    'fname', 'lname', 'mi', 'phone1', 'phone2',
                                    'contact_email', 'time_to_reach']}),
        ('ACME', {'fields': ['diagnosis', 'near_clinic', 'pregnant', 'facial_hair',
                             'stop_rx', 'contact_att1', 'contact_att2', 'status',
                             'accepted']}),
    ]
    list_display = ['fname', 'lname', 'status']
    list_filter = ['status']


admin.site.register(ACME_Rosacea, ACME_Rosacea_Contacts)

class StarFleet_Di_Li_Contacts(admin.ModelAdmin):
    fieldsets = [
        ('Call Center', {'fields': ['site', 'contact_date', 'lead_type',
                                    'fname', 'lname', 'mi', 'phone1', 'phone2',
                                    'contact_email', 'time_to_reach']}),
        ('Star Fleet',  {'fields': ['years_in_space', 'work_in_engineeriing',
                                    'exposed_to_di_li', 'contact_att1',
                                    'contact_att2', 'status', 'accepted']})
    ]
    list_display = ['fname', 'lname', 'status']
    list_filter = ['status']

admin.site.register(StarFleet_Di_Li, StarFleet_Di_Li_Contacts)

## End admin.py


