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
		print 'user',username,password
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
		print'dates',today_date,weekago_date
		# pending_contacts_list = []
		# today = datetime.date.today()
		# week_ago = today - datetime.timedelta(days=7)
		# print'>>',today,week_ago
		users_dict={'id':'','first_name':'','last_name':'','status':''} 
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
				users_dict["status"] = user.status
				users_list.append(users_dict.copy())
			today_contacts = ACME_T2D.objects.filter(contact_date = today_date) 
			for contacts in today_contacts:
				today_contacts_dict['id']=contacts.id
				today_contacts_dict["first_name"] = contacts.fname
				today_contacts_dict["last_name"] = contacts.lname
				today_contacts_dict["time_to_reach"] = contacts.time_to_reach
				today_contacts_list.append(today_contacts_dict.copy())
			print 'today_contacts_list',today_contacts_list
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
			status =data_dict['new_status'])
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
			print 'data_dict',data_dict
			usr_evnt_obj = UserEvents.objects.create(title=data_dict['title'],
			start_date=data_dict['start'],end_date=data_dict['end'],
			user=request.user)
			print 'usr_evnt_obj',usr_evnt_obj
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
		print 'response_list',response_list
		return JsonResponse(final_response)
	except Exception as e:
		print 'error',e

# update event
@csrf_exempt
def updateEvent(request):
	try:
		if request.method == 'POST':
			data_dict = json.loads(request.body)
			print 'data_dict',data_dict
			start = data_dict['start']
			end = data_dict['end']
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
			print 'data_dict',data_dict
			event_id = data_dict['event_id']
			UserEvents.objects.filter(pk=event_id).delete()
			return JsonResponse({'status':'success'})
	except Exception as e:
		print 'error',e


#Get Chart Data
@csrf_exempt
def getChartData(request):
	try:
		print 'shashank'
		today_date =datetime.date.today()
		weekago_date=datetime.date.today()+timedelta(-7)
		print 'today_date',today_date
		print 'weekago_date',weekago_date
		modal_object =  ACME_T2D.objects.filter(contact_date__range=(weekago_date,today_date))
		print 'modal_object',modal_object
		response_dict = {'leads_by_ienroll':'','leads_fialed_screeing':'',
		'leads_enrolled_successfully':''}
		failed_lead_list = []
		lead_sentby_enroll_list = []
		success_lead_list = []
		start_date = datetime.datetime.now()+timedelta(-30)
		end_date = datetime.datetime.now()
		###########  Leads send by enroll through web form #############
		obj = ACME_T2D.objects.filter(lead_type="web_form").filter(contact_date__range=(start_date,end_date))
		if obj:
			for date in obj:
				lead_sentby_enroll_list.append(date.contact_date.strftime('%Y,%m,%d'))	
			lead_sentby_enroll_dict = dict(Counter(lead_sentby_enroll_list))
			lead_sentby_enroll_list = dict_object_creator(lead_sentby_enroll_dict)
			response_dict['leads_by_ienroll']=lead_sentby_enroll_list
		# ############ Failed Leads  #############
		failed_lead = ACME_T2D.objects.filter(notes='fail_ienroll').filter(contact_date__range=(start_date,end_date))
		if failed_lead:
			for data in failed_lead:
				failed_lead_list.append(data.contact_date.strftime('%Y,%m,%d'))
			failed_lead_dict = dict(Counter(failed_lead_list))
			failed_lead_list = dict_object_creator(failed_lead_dict)
			response_dict['leads_fialed_screeing']=failed_lead_list
		# ########## successfull lead  #################
		success_lead = ACME_T2D.objects.filter(notes="enrolled").filter(contact_date__range=(start_date,end_date))
		if success_lead:
			for val in success_lead:
				success_lead_list.append(val.contact_date.strftime('%Y,%m,%d'))
			success_lead_dict = dict(Counter(success_lead_list))
			success_lead_list = dict_object_creator(success_lead_dict)
			response_dict['leads_enrolled_successfully']=success_lead_list
		# print json.dumps(response_dict, sort_keys=True,indent=4, separators=(',', ': '))
		return JsonResponse(response_dict)	
	except Exception as e:
		print 'error',e				


def dict_object_creator(input_dict):
	try:
		result = []
		result_dict = {'date':'','value':''}
		for key ,val in input_dict.items():
			result_dict['date']=key
			result_dict['value']=val
			result.append(result_dict.copy())
		return 	result
	except Exception as e:
		print 'error',e

		