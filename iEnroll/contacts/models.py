# contacts/models.py - DB layout ('models') for the iEnroll contacts db
#
# David R. McWilliams <dave@suemac.org>
# 09-Feb-2017 Intitiate

from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (('AL', 'Alabama'),
                 ('AK', 'Alaska'),
                 ('AZ', 'Arizona'),
                 ('AR', 'Arkansas'),
                 ('CA', 'California'),
                 ('CO', 'Colorado'),
                 ('CT', 'Connecticut'),
                 ('DE', 'Delaware'),
                 ('DC', 'District of Columbia'),
                 ('FL', 'Florida'),
                 ('GA', 'Georgia'),
                 ('HI', 'Hawaii'),
                 ('ID', 'Idaho'),
                 ('IL', 'Illinois'),
                 ('IN', 'Indiana'),
                 ('IA', 'Iowa'),
                 ('KS', 'Kansas'),
                 ('KY', 'Kentucky'),
                 ('LA', 'Louisiana'),
                 ('ME', 'Maine'),
                 ('MD', 'Maryland'),
                 ('MA', 'Massachusetts'),
                 ('MI', 'Michigan'),
                 ('MN', 'Minnesota'),
                 ('MS', 'Mississippi'),
                 ('MO', 'Missouri'),
                 ('MT', 'Montana'),
                 ('NE', 'Nebraska'),
                 ('NV', 'Nevada'),
                 ('NH', 'New Hampshire'),
                 ('NJ', 'New Jersey'),
                 ('NM', 'New Mexico'),
                 ('NY', 'New York'),
                 ('NC', 'North Carolina'),
                 ('ND', 'North Dakota'),
                 ('OH', 'Ohio'),
                 ('OK', 'Oklahoma'),
                 ('OR', 'Oregon'),
                 ('PA', 'Pennsylvania'),
                 ('RI', 'Rhode Island'),
                 ('SC', 'South Carolina'),
                 ('SD', 'South Dakota'),
                 ('TN', 'Tennessee'),
                 ('TX', 'Texas'),
                 ('UT', 'Utah'),
                 ('VT', 'Vermont'),
                 ('VA', 'Virginia'),
                 ('WA', 'Washington'),
                 ('WV', 'West Virginia'),
                 ('WI', 'Wisconsin'),
                 ('WY', 'Wyoming'),
                 ('PR', 'Puerto Rico'),
                 ('VI', 'U.S. Virgin Islands'),)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=25)
    state = models.CharField(choices=STATE_CHOICES, max_length=2)
    contact_fname = models.CharField(max_length=10, verbose_name="Contact First Name")
    contact_lname = models.CharField(max_length=15, verbose_name="Contact Last Name")
    contact_mi = models.CharField(max_length=1, verbose_name="Contact Middle Initial", blank=True, null=True)
    # ToDo: Provide or enforce a phone number format
    contact_ph1 = models.CharField(max_length=15, verbose_name="Phone1")
    contact_ph2 = models.CharField(max_length=15, verbose_name="Phone2", blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'

class Trials(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    contract_id = models.CharField(max_length=15)
    start_date  = models.DateField()
    end_date    = models.DateField(blank=True, null=True)
    acceptance_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Trial'
        verbose_name_plural = 'Trials'

class ACME_T2D(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    site     = models.CharField(max_length=25, blank=True,
                                choices=(('Charlotte', 'Charlotte'),
                                         ('Raleigh', 'Raleigh'),
                                         ('WS', 'Winston-Salem')),
                                default='Charlotte')
    contact_date = models.DateField()
    lead_type = models.CharField(max_length=10, blank=True, null=True,
                                 choices=(('call', 'Call'),('webform', 'WebForm')))
    fname = models.CharField(max_length=10, verbose_name="Contact First Name")
    lname = models.CharField(max_length=15, verbose_name="Contact Last Name")
    mi = models.CharField(max_length=1, verbose_name="Contact Middle Initial", blank=True, null=True)
    phone1 = models.CharField(max_length=15, verbose_name="Phone1")
    phone2 = models.CharField(max_length=15, verbose_name="Phone2", blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    time_to_reach = models.CharField(max_length=50, blank=True, null=True,
                                     choices = (('any', 'Any'),
                                                ('morning', 'Morning'),
                                                ('noon', 'Noon'),
                                                ('afternoon', 'Afternoon'),
                                                ('evening', 'Evening')),
                                     default = 'afternoon')
    near_clinic = models.NullBooleanField(default=False)
    diagnosis = models.CharField(max_length=25, blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Height (inches)")
    weight = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Weight (pounds)")
    triglycerides = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    lipids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pulse = models.PositiveSmallIntegerField(blank=True, null=True)
    bp    = models.CharField(max_length=7, blank=True, null=True)
    notes = models.TextField(max_length=512, blank=True, null=True)
    reviewed = models.BooleanField(default=False)
    status = models.CharField(max_length=25, default='pending',
                              choices=(('pending_customer', 'Pending Customer Review'),
                                       ('screened_ienroll', 'Screened by iEnroll'),
                                       ('fail_ienroll', 'Failed iEnroll Screen'),
                                       ('fail_client',  'Fail Client Screen'),
                                       ('too_far', 'Not Interested, Too Far'),
                                       ('placebo', 'Not Intereseted, Placebo'),
                                       ('enrolled', 'Enrolled')))
    accepted = models.BooleanField(default=False)

    def __str__(self):
        tag = self.fname + " " + self.lname + " -- " + self.status
        return tag

    class Meta:
        verbose_name = 'ACME_T2D'


class ACME_Rosacea(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_date = models.DateField()
    site = models.CharField(max_length=25, choices= (('FV', 'Fuquay-Varina'),
                                                     ('Bahama', 'Bahama'),
                                                     ('Mills', 'Mills River')),
                            default='FV')
    lead_type = models.CharField(max_length=10, blank=True, null=True, choices=(('call', 'Call'),('webform', 'WebForm')))
    fname = models.CharField(max_length=10, verbose_name="Contact First Name")
    lname = models.CharField(max_length=15, verbose_name="Contact Last Name")
    mi = models.CharField(max_length=1, verbose_name="Contact Middle Initial", blank=True, null=True)
    phone1 = models.CharField(max_length=15, verbose_name="Phone1")
    phone2 = models.CharField(max_length=15, verbose_name="Phone2", blank=True, null=True)
    contact_email = models.EmailField()
    time_to_reach = models.DurationField(blank=True, null=True)
    diagnosis = models.CharField(max_length=25, blank=True, null=True)
    near_clinic = models.NullBooleanField(default=False)
    pregnant = models.NullBooleanField(default=False)
    facial_hair = models.NullBooleanField(default=False)
    stop_rx = models.NullBooleanField(default=False, verbose_name="Willing to stop Rx")
    contact_att1 = models.CharField(max_length=15,
                                    choices=(
                                        ('successful', 'Successful'),
                                        ('message', 'Message'),
                                        ('no_answer', 'No Answer')))
    contact_att2 = models.CharField(max_length=15,
                                    choices=(
                                        ('successful', 'Successful'),
                                        ('message', 'Message'),
                                        ('no_answer', 'No Answer')))
    status = models.CharField(max_length=15, default='pending',
                              choices=(('pending', 'Pending'),
                                       ('screened_ienroll', 'Screened by iEnroll'),
                                       ('fail_ienroll', 'Failed iEnroll Screen'),
                                       ('fail_client',  'Fail Client Screen'),
                                       ('too_far', 'Not Interested, Too Far'),
                                       ('placebo', 'Not Intereseted, Placebo'),
                                       ('enrolled', 'Enrolled')))
    accepted = models.BooleanField(default=False)

    def __str__(self):
        tag = self.fname + " " + self.lname + " -- " + self.status
        return tag

    class Meta:
        verbose_name = 'ACME_Rosacea'

class StarFleet_Di_Li(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    site = models.CharField(max_length=25, choices= (('Earth', 'Earth'),
                                                     ('Vulcan', 'Vulcan'),
                                                     ('Kronos', 'Kronos'),
                                                     ('other', 'Other')),
                            default='Earth')
    contact_date = models.DateField()
    lead_type = models.CharField(max_length=10, blank=True, null=True, choices=(('call', 'Call'),('webform', 'WebForm')))
    fname = models.CharField(max_length=10, verbose_name="Contact First Name")
    lname = models.CharField(max_length=15, verbose_name="Contact Last Name")
    mi = models.CharField(max_length=1, verbose_name="Contact Middle Initial", blank=True, null=True)
    phone1 = models.CharField(max_length=15, verbose_name="Phone1")
    phone2 = models.CharField(max_length=15, verbose_name="Phone2", blank=True, null=True)
    contact_email = models.EmailField()
    time_to_reach = models.DurationField(blank=True, null=True)
    years_in_space = models.PositiveSmallIntegerField(blank=True, null=True)
    work_in_engineeriing = models.BooleanField(default=False)
    exposed_to_di_li = models.BooleanField(default=False)
    contact_att1 = models.CharField(max_length=15,
                                    choices=(
                                        ('successful', 'Successful'),
                                        ('message', 'Message'),
                                        ('no_answer', 'No Answer')))
    contact_att2 = models.CharField(max_length=15,
                                    choices=(
                                        ('successful', 'Successful'),
                                        ('message', 'Message'),
                                        ('no_answer', 'No Answer')))

    status = models.CharField(max_length=15, default='pending',
                              choices=(('pending', 'Pending'),
                                       ('screened_ienroll', 'Screened by iEnroll'),
                                       ('fail_ienroll', 'Failed iEnroll Screen'),
                                       ('fail_client',  'Fail Client Screen'),
                                       ('too_far', 'Not Interested, Too Far'),
                                       ('placebo', 'Not Intereseted, Placebo'),
                                       ('enrolled', 'Enrolled')))
    accepted = models.BooleanField(default=False)

    def __str__(self):
        tag = self.fname + " " + self.lname + " -- " + self.status
        return tag

    class Meta:
        verbose_name = 'StarFleet_Di_Li'

class UserEvents(models.Model):
    title=models.CharField(max_length=256)
    start_date=models.DateTimeField()   
    end_date=models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE) 