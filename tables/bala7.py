import csv
import re
import pdb
from .models import *

#table = open('tabula-Year-3 IS.csv')

def generate_table(table, department_id): 	#accepts csv table

	tableCSV = csv.reader(table)

    ###extracting data
	data = list(tableCSV)
	row_count = len(data)
	for i in range(1, row_count+1):
		sec_name = 'سكشن '+str(i)
		Section.objects.create(name = sec_name, department = department_id)
	week = list()
	day = list()
	week_days = list()
	week_end = 7
	for day in range(4, -1, -1):
		for row in range(row_count-1, -1, -1):
			for col in range(week_end-7, week_end):
				if data[row][col] == '':
					week_days.append('empty')
				else:
					week_days.append(data[row][col])
		week.append(week_days)
		week_days = list()
		week_end = week_end+7
	###right-to-left support
	week.reverse()
	for day in week:
		day.reverse()
	return week




#TODO::reverse week and periods 

def day_query(days):	
	############## querying using day ##############

	query = 'monday, tuesday' #should be replaced by stdinput 
	if query == 'monday, tuesday':

		#TODO::split input string

		days = [3, 4]
		for day in days:
			for period in week[day-1]:
				cont.write(period)
			cont.write('\n********************\n')
		pass

def group_query(group_id):

	############## querying using group ##############
	query_group_id = group_id					#should be replaced by stdinput
	col_start = (query_group_id-1)*7
	col_end = col_start+7
	for day in week:
		for i in range(col_start, col_end):
			cont.write(day[i])
		cont.write('\n********************\n')


def extract_subjects(week):
	all_array = str()
	for day in week:
		for period in day:
			all_array = all_array +' '+ period

	subjects_list = list() 
	for day in week:
		for period in day:
			if re.match(r'\u0627\u0644\u0641\u0631\u0642\u0629\s*\u0627\u0644\u062b\u0627\u0644\u062b\u0629-\s*\u0646\u0638\u0645', period):
				subjects_list.append(period)
	return subjects_list


def subject_day(week):

	############## querying using day & subject ##############	

	### extracting subjects ### 
	all_array = str()
	for day in week:
		for period in day:
			all_array = all_array +' '+ period

	### Regex method ###
	#test = re.findall(r'\u0627\u0644\u0641\u0631\u0642\u0629\s*\u0627\u0644\u062b\u0627\u0644\u062b\u0629-\s*\u0646\u0638\u0645\s(.*\s){3}', all_array)
	#test = re.findall(r'\(\d\)\s$', all_array)

	subjects_list = list() 
	for day in week:
		for period in day:
			if re.match(r'\u0627\u0644\u0641\u0631\u0642\u0629\s*\u0627\u0644\u062b\u0627\u0644\u062b\u0629-\s*\u0646\u0638\u0645', period):
				subjects_list.append(period)

	subjects = list(set(subjects_list))
	query_days = [1]
	query_subjects = [2, 3]
	# Displaying each matched result to queries 
	results = list()
	target_days = list()

	for target in query_days:
		target_days.append(week[target-1])

	for day in target_days:
		for period in day:
			for query in query_subjects:
				if period == subjects[query]:
					print(day.index(period))
					results.append(period+'\n'+get_period_time(day.index(period)))

	for result in results:
		cont.write(result+'\n')

def get_period_time(postion):
	return 'الفترة'+str(7-postion)	#return position after reverse days



