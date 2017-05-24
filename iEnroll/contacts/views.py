# contacts/views.py - Views for the iEnroll/contacts app
#
# David R. McWilliams <dave@suemac.org>
# 09-Feb-2017 Initiate

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import ACME_T2D_ContactForm
from .models import ACME_T2D, Customer

def index(request):
    '''Home page view.'''
    return render(request, 'contacts/index.html')


# 14-Feb-2017
# @login_required
def acme_t2d(request):
    '''Update contact info for the ACME_T2D trial.'''

    if request.method == 'POST':
        form = ACME_T2D_ContactForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            customer = Customer.objects.get(pk=1) # Since this form is particular to a customer
            site = form.cleaned_data['site']
            contact_date = form.cleaned_data['contact_date']
            lead_type = form.cleaned_data['lead_type']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            mi = form.cleaned_data['mi']
            phone1 = form.cleaned_data['phone1']
            phone2 = form.cleaned_data['phone2']
            contact_email = form.cleaned_data['contact_email']
            time_to_reach = form.cleaned_data['time_to_reach']
            near_clinic = form.cleaned_data['near_clinic']
            diagnosis = form.cleaned_data['diagnosis']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            triglycerides = form.cleaned_data['triglycerides']
            lipids = form.cleaned_data['lipids']
            pulse = form.cleaned_data['pulse']
            bp = form.cleaned_data['bp']
            status = form.cleaned_data['status']
            accepted = form.cleaned_data['accepted']
            notes = form.cleaned_data['notes']
            reviewed = form.cleaned_data['reviewed']

            contact = ACME_T2D()

            contact.customer = customer
            contact.site = site
            contact.contact_date = contact_date
            contact.lead_type = lead_type
            contact.fname = fname
            contact.lname = lname
            contact.mi = mi
            contact.phone1 = phone1
            contact.phone2 = phone2
            contact.contact_email = contact_email
            contact.time_to_reach = time_to_reach
            contact.near_clinic = near_clinic
            contact.diagnosis = diagnosis
            contact.height = height
            contact.weight = weight
            contact.triglycerides = triglycerides
            contact.lipids = lipids
            contact.pulse = pulse
            contact.bp = bp
            contact.status = status
            contact.accepted = accepted
            contact.notes = notes
            contact.reviewed = reviewed

            contact.save()

            # redirect to a new URL:
            return HttpResponseRedirect('thanks.html')

    else:
        form = ACME_T2D_ContactForm()

    return render(request, 'contacts/acme_t2d.html', {'form': form})

def thanks(request):
    return render (request, 'contacts/thanks.html')

def about(request):
    return render(request, 'contacts/about.html')

from django.db.models import Count
def contacts_summary(request):
    status_list = ACME_T2D.objects.values('status').annotate(status_cnt=Count('status'))
    context = {'status_list':status_list}
    return render(request, 'contacts/contacts_summary.html', context)

# End contacts/views.py
