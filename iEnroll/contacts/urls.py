# contacts/urls.py - urlconf for iEnroll/contacts
#
# David R. McWilliams <dave@suemac.org>
# 09-Feb-2017 Initiate

from django.conf.urls import url

from . import views

app_name = 'contacts'
urlpatterns = [
    url(r'^$',        views.index, name="index"),
    url(r'^index',    views.index, name="index"),
    url(r'^home',     views.index, name="index"),
    url(r'^about',    views.about, name="about"),
    url(r'^acme_t2d/$', views.acme_t2d, name="acme_t2d"),
    url(r'^acme_t2d/contacts_summary', views.contacts_summary, name='contacts_summary'),
    url(r'^thanks',   views.thanks, name="thanks"),
]
