from django.db import models

# Create your models here.
class University(models.Model):
	name = models.CharField(max_length=200)
	rank = models.IntegerField()

	def __str__(self):
		return self.name

class Faculty(models.Model):
	name = models.CharField(max_length=200)
	university = models.ForeignKey(University, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=200)
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
	off_days = models.CharField(max_length=5)
	def __str__(self):
		return self.name

class Section(models.Model):
	name = models.CharField(max_length=200)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=200)
	department = models.ManyToManyField(Department)

	def __str__(self):
		return self.name
		

class table(models.Model):
	subject = models.CharField(max_length=500)
	day = models.IntegerField()
	section = models.ForeignKey(Section, related_name = 'data_section', on_delete = models.CASCADE)
	period = models.IntegerField()
	department = models.ForeignKey(Department, related_name='table_department', on_delete = models.CASCADE)
	
class Visitor(models.Model):
	email = models.CharField(max_length=250)
	active = models.IntegerField()
		