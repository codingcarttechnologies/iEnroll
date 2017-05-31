from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from contacts.models import ACME_T2D,UserEvents
from django.template.loader import render_to_string
from datetime import datetime,timedelta
from django.db.models import Count
from collections import Counter
import datetime

# Admin Login page rendering
@csrf_exempt
def adminLogin(request):
	try:
		if request.method == 'GET':
			return render(request,'accounts/admin_customlogin.html',context={})
		else:
			pass
	except Exception as e:
		print 'error',e


#Authentication Function
@csrf_exempt
def authenticateUser(request):
	try:
		data_dict = json.loads(request.body)
		username = data_dict['username']
		password = data_dict['password']
		user=User.objects.filter(username=username)
		for us in user:
			user_password=us.password
			check=check_password(password,user_password)
		if check is True:
			try:
				new_user = authenticate(username=username, password=password)
			except Exception as e:
				print 'error',e	
			if new_user:
				auth_login(request, new_user)
				return HttpResponse('authentic')
			else:
				return HttpResponse('non-authentic')
		else:
			return HttpResponse('non-authentic')
	except Exception as e:
		return HttpResponse('non-authentic')


# Dashboard Controller
@csrf_exempt
def adminDashboard(request):	
	try:
		users_list=[]
		today_contacts_list=[]
		pending_contacts_list=[]
		today_date = datetime.date.today()
		weekago_date = datetime.date.today()+timedelta(-7)
		users_dict={'id':'','first_name':'','last_name':'','status':'','tracking':'','email':''} 
		today_contacts_dict =  {'id':'','first_name':'','last_name':'','time_to_reach' : ''} 
		pending_contacts_dict =  {'id':'','first_name':'','last_name':'','time_to_reach' : '','scheduled_date':''} 	
		if (request.user.id != None):	
			users = ACME_T2D.objects.all()
			pending_contacts = ACME_T2D.objects.filter(reviewed = False).filter(contact_date__range = (weekago_date,today_date))
			for contact in pending_contacts:
				pending_contacts_dict['id']=contact.id
				pending_contacts_dict["first_name"] = contact.fname
				pending_contacts_dict["last_name"] = contact.lname
				pending_contacts_dict["time_to_reach"] = contact.time_to_reach
				pending_contacts_dict["scheduled_date"] = contact.contact_date
				pending_contacts_list.append(pending_contacts_dict.copy())
			for user in users:
				users_dict['id']=user.id
				users_dict["first_name"] = user.fname
				users_dict["last_name"] = user.lname
				users_dict["email"] = user.contact_email
				users_dict["status"] = user.status
				users_dict["tracking"] = user.tracking
				users_list.append(users_dict.copy())
			today_contacts = ACME_T2D.objects.filter(contact_date = today_date) 
			for contacts in today_contacts:
				today_contacts_dict['id']=contacts.id
				today_contacts_dict["first_name"] = contacts.fname
				today_contacts_dict["last_name"] = contacts.lname
				today_contacts_dict["time_to_reach"] = contacts.time_to_reach
				today_contacts_list.append(today_contacts_dict.copy())
			return render(request,'admin/custom.html',{'user':request.user,'users_data':users_list,
				'pending_contacts':pending_contacts_list,'today_contacts':today_contacts_list})	
		else:	
			return HttpResponseRedirect("/admin/")
	except Exception as e:		
		print 'error',e

# Delete User
@csrf_exempt
def deleteUser(request):	
	try:
		data_dict = json.loads(request.body)
		user_id = data_dict['user_id']
		ACME_T2D.objects.filter(id=user_id).delete()
		return HttpResponse("success")
	except Exception as e:
		print 'error',e

# Update User
@csrf_exempt
def updateUser(request):	
	try:
		data_dict = json.loads(request.body)
		user_id = data_dict['user_id']
		ACME_T2D.objects.filter(id=user_id).update(fname = data_dict['new_fname'],lname = data_dict['new_lname'],
			status =data_dict['new_status'],tracking=data_dict['new_tracking'],contact_email=data_dict['new_email'])
		return HttpResponse("success")
	except Exception as e:
		print 'error',e



# LogOut Controller
@csrf_exempt
def logout(request):	
	try:		
		request.user=''		
		auth_logout(request)		
		return HttpResponseRedirect("/admin_new/")		
	except Exception as e:		
		print 'error',e


#Add new user to ACME_T2D table
@csrf_exempt
def addUser(request):
	try:
		if request.method == 'POST':
			data_dict = json.loads(request.body)
	except Exception as e:
		print 'error',e	

# create new event 
@csrf_exempt
def creatEvent(request):
	try:
		if request.method == 'POST':
			data_dict = json.loads(request.body)
			start = datetime.datetime.strptime(data_dict['start'], '%Y-%m-%d %I:%M %p')
			end = datetime.datetime.strptime(data_dict['end'], '%Y-%m-%d %I:%M %p')
			usr_evnt_obj = UserEvents.objects.create(title=data_dict['title'],
			start_date=start,end_date=end,
			user=request.user)
			usr_evnt_obj.save()
			return JsonResponse({'_id':usr_evnt_obj.id})
	except Exception as e:
		print 'error',e	

# get all events
@csrf_exempt
def getEvents(request):
	try:
		final_response = {}
		data_dict = json.loads(request.body)
		response_list = []
		response_dict = {'title':'','start':'','end':'','_id':'','allDay':False}
		tb_usr_evnt = UserEvents.objects.filter(user_id=data_dict['user_id'])
		for obj in tb_usr_evnt:
			response_dict['_id']=obj.id
			response_dict['title']=obj.title
			response_dict['start']=obj.start_date.strftime("%Y-%m-%d %H:%M:%S")
			response_dict['end']=obj.end_date.strftime("%Y-%m-%d %H:%M:%S")
			response_list.append(response_dict.copy())
		final_response['data']=	response_list
		return JsonResponse(final_response)
	except Exception as e:
		print 'error',e

# update event
@csrf_exempt
def updateEvent(request):
	try:
		if request.method == 'POST':
			data_dict = json.loads(request.body)
			start = datetime.datetime.strptime(data_dict['start'], '%Y-%m-%d %I:%M %p')
			end = datetime.datetime.strptime(data_dict['end'], '%Y-%m-%d %I:%M %p')
			title = data_dict['title']
			event_id = data_dict['event_id']
			UserEvents.objects.filter(pk=event_id).filter(user=request.user).update(title=title,
				start_date=start,end_date=end)
			return JsonResponse({'status':'success'})
	except Exception as e:
		print 'error',e


# Delete event
@csrf_exempt
def deleteEvent(request):
	try:
		if request.method == 'POST':
			data_dict = json.loads(request.body)
			event_id = data_dict['event_id']
			UserEvents.objects.filter(pk=event_id).delete()
			return JsonResponse({'status':'success'})
	except Exception as e:
		print 'error',e


#Get Chart Data
@csrf_exempt
def getChartData(request):
	try:
		response_list =[]
		response_dict = {'category':'','count':''}
		pending_leads = ACME_T2D.objects.filter(status="pending").count()
		noresponse_leads = ACME_T2D.objects.filter(status="no_response").count()
		fail_verbal_leads = ACME_T2D.objects.filter(status="fail_verbal_pre-screening").count()
		fail_clinic_leads = ACME_T2D.objects.filter(status="fail_clinic_screening").count()
		declined_leads = ACME_T2D.objects.filter(status="declined").count()
		enrolled_leads = ACME_T2D.objects.filter(status="enrolled").count()
		if noresponse_leads:
				response_dict['category']='No Response'
				response_dict['count']=noresponse_leads
				response_list.append(response_dict.copy())
		if pending_leads:
			response_dict['category']='Pending'
			response_dict['count']=pending_leads
			response_list.append(response_dict.copy())		
		if fail_verbal_leads:
				response_dict['category']='Failed Verbal'
				response_dict['count']=fail_verbal_leads
				response_list.append(response_dict.copy())
		if declined_leads:
				response_dict['category']='Declined'
				response_dict['count']=declined_leads
				response_list.append(response_dict.copy())
		if enrolled_leads:
				response_dict['category']='Enrolled'
				response_dict['count']=enrolled_leads
				response_list.append(response_dict.copy())
		if fail_clinic_leads:
				response_dict['category']='Failed Clinic'
				response_dict['count']=fail_clinic_leads
				response_list.append(response_dict.copy())												
		return JsonResponse({'chartData':response_list})					
	except Exception as e:
		print 'error',e				


#Update table using ajax 
@csrf_exempt
def update_table_ajax(request):
	try:
		users_list=[]
		users_dict={'id':'','first_name':'','last_name':'','status':'','tracking':'','email':''} 
		if (request.user.id != None) and request.method == 'POST':
			users = ACME_T2D.objects.all()
			for user in users:
				users_dict['id']=user.id
				users_dict["first_name"] = user.fname
				users_dict["last_name"] = user.lname
				users_dict["status"] = user.status
				users_dict["tracking"] = user.tracking
				users_dict["email"] = user.contact_email
				users_list.append(users_dict.copy())
			html = render_to_string('admin/update_table_ajax.html', {'user':request.user,'users_data':users_list})		
			return HttpResponse(html)
		else:
			return HttpResponseRedirect("/admin/")		
	except Exception as e:
		print 'error',e    
		