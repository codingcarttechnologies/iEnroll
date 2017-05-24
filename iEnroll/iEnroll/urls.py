"""iEnroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^contacts/', include('contacts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin_new/', views.adminLogin, name='admin_login'),
    url(r'^authenticateUser/$', views.authenticateUser, name='authenticateUser'),
    url(r'^dashboard/$', views.adminDashboard, name='adminDashboard'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^deleteUser/$', views.deleteUser, name='deleteUser'),
    url(r'^updateUser/$', views.updateUser, name='updateUser'),
    url(r'^addUser/$', views.addUser, name='addUser'),
    url(r'^create-event/$', views.creatEvent, name='creatEvent'),
    url(r'^get-events/$', views.getEvents, name='getEvents'),
    url(r'^update-event/$', views.updateEvent, name='updateEvent'),
    url(r'^get-chartdata/$', views.getChartData, name='getChartData'),

]

