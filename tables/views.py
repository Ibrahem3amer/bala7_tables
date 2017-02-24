from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import *
import json
from tables.bala7 import generate_table
from django.core.files import File
import re
from django.template.defaulttags import register

# customized template filters and tags 

@register.filter
def display_week(dictionary, key):
    return dictionary.get(key)

@register.filter
def display_week_sun(dictionary, key):
    return dictionary.get(key+1)

@register.filter
def subtract(value, arg):
    return value - arg


# Create your views here.

def index(request):
	univers = University.objects.all()
	faculties = Faculty.objects.all()
	departments = Department.objects.all()
	return render(request, 'tables/home.html', {'univs': univers, 'faculty': faculties, 'departments': departments})

### Ajax Callbacks ###

def get_faculties(request):
	data = request.GET.get("uni_id", "")
	f_list = list()
	data_list = serializers.serialize("json", Faculty.objects.filter(university =  data), fields=('pk', 'name'))
	return HttpResponse(data_list)


def get_departments(request):
	data = request.GET.get("fac_id", "")
	f_list = list()
	data_list = serializers.serialize("json", Department.objects.filter(faculty =  data), fields=('pk', 'name'))
	return HttpResponse(data_list)

###

# Get input and display results
def get_input(request):
	university_id = request.GET.__getitem__('university')
	faculty_id = request.GET.__getitem__('faculties')
	department_id = request.GET.__getitem__('departments')
	request.session['university_id'] = university_id
	request.session['faculty_id'] = faculty_id
	request.session['department_id'] = department_id
	department = Department.objects.get( pk = department_id )
	flag = 0
	if department.off_days == 'sat':
		flag = 1
	subjects = Subject.objects.filter(department = Department.objects.get(pk = department_id)) 	#inner join
	sections = Section.objects.filter(department = Department.objects.get(pk = department_id))	#outer join

	return render(request, 'tables/form.html', {'subjects': subjects, 'sections': sections, 'off_days': flag})

def get_results(request):
	days = request.GET.getlist('day')
	subjects = request.GET.getlist('subject')
	sections = request.GET.getlist('section')
	department = request.session['department_id']
	department_checker = Department.objects.get( pk = department )	#retreive data
	flag = 0
	if department_checker.off_days == 'sat':
		flag = 1
	visitor_email = request.GET.__getitem__('user_email')
	visitor_q = Visitor.objects.filter(email = visitor_email).exists()
	if visitor_q:
		visitor_q = Visitor.objects.get(email = visitor_email)
		visitor_q.active += 1
		visitor_q.save()
	else:
		visitor_q = Visitor.objects.create(email = visitor_email, active = 1)
	loop_counter = 0
	query = list()
	week_days = {0: 'السبت', 1: 'الأحد', 2: 'الإثنين', 3: 'الثلاثاء', 4: 'الأربعاء', 5: 'الخميس'}
	times = {1: '8:30 - الأولى', 2: '10:05 - التانية', 3: '11:40 - التالتة', 4: '1:30 - الرابعة', 5: '3:05 - الخامسة', 6: '4:40 - السادسة', 7: '6:10 - السابعة'}
	inputs = {}
	if days:
		inputs['day__in'] = days
	if sections:
		inputs['section__in'] = sections
	if not subjects:
		arr = []
		subjects = list(Subject.objects.filter(department = department))
		for s in subjects:
			arr.append(str(s))
		subjects = arr
	for subject in subjects:
		sub = subject.split(' ')
		if len(sub) <= 1:
			regex_expression = r""+sub[0]+"\n"
		else:
			regex_expression = r""+sub[0]+"\s"+sub[1]+""
		inputs['subject__regex'] = regex_expression
		query += list(table.objects.filter(**inputs).order_by('day'))
		loop_counter += 1		
	if len(query) > 0 :
		return render(request, 'tables/results.html', {'results': query, 'week_days': week_days, 'times': times, 'off_days': flag})
	else:
		return render(request, 'tables/results_no.html')


###



### Seeding

def seeding_subjects(request):
	'''
		* now it can iterate through file and figure out departments
		* it can figure out subjects names as well 

		***TODO***
		* Assign each subject to certain department (depar variable) --done
		* Check when you have shared subjects (if(line[0] == 40)) --done
		* Seperate each department and assign this subjects for both --done
	'''
	file_url = 'tables/'+request.GET.__getitem__('file_name')+'.txt'
	subjects = open(file_url, 'rb')
	for line in subjects:
		if( line == bytes('-------------------------------\n', 'utf-8')):	#ready to accept subject name
			name = str(bytes(next(subjects, None)), 'utf-8').strip('\n')
			depar = Department.objects.get( name__icontains = name )
		else:
			shared_departments = ''
			i = 1
			if( line[0] == 40 ):
				while(line[i] != 41):
					shared_departments += chr(line[i])
					i += 1
				department_list = shared_departments.split('&')
				for d in department_list:
					name_line = str(line, encoding='UTF-8').strip('\n')
					name_trimmed = name_line.split(')')
					department = Department.objects.get( name__iexact = d )
					s = Subject.objects.create( name = name_trimmed[1] )	#creation query
					s.department.add(department)				#foreign key relation
			else:
				sub = str(line, encoding='UTF-8').strip('\n')
				s = Subject.objects.create( name = sub )			#transaction
				s.department.add(depar)

	return HttpResponse('done')

def seeding_table(request):
	table_url = 'tables/tables_data/'+request.GET.__getitem__('tablename')+'.csv'
	table_is = open(table_url, 'r')
	department_id = Department.objects.get(pk = request.GET.__getitem__('department'))		#to be chosen dinamically
	week = generate_table(table_is, department_id)
	day_counter = 0
	for day in week:
		section_counter = 1
		section_incremental = 1
		period_counter = 1
		for period in day:
			section_name = 'سكشن '+str(section_counter)
			section = Section.objects.get(name__exact = section_name, department = department_id)
			table.objects.create(subject = period, day = day_counter, section = section, period = period_counter, department = department_id)
			if (section_incremental)%7 == 0:
				section_counter += 1
				period_counter = 0
			section_incremental += 1
			period_counter += 1
		day_counter += 1
	return HttpResponse('done')


