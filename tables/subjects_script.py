#from .models import *
from itertools import islice

subjects = open('subjects.txt', 'rb')
arr = list()
dep = ''
for line in subjects:
	if( line == bytes('-------------------------------\n', 'utf-8')):	#ready to accept subject name
		print(next(subjects, None).decode('utf-8'))
	else:
		i = 1
		if( line[0] == 40 ):
			print(chr(line[1]))
			while(line[i] != 41):
				dep += chr(line[i])
				i += 1
	