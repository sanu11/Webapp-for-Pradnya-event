from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Junior(models.Model):
	user1=models.CharField(max_length=15)
	user2=models.CharField(max_length=15)
	college=models.CharField(max_length=20)
	phone=models.CharField(max_length=12)
	email=models.EmailField(max_length=50,unique=True)
	password=models.CharField(max_length=25)
	score=models.IntegerField(default=0)
	logintime=models.IntegerField(default=0)
	timestamp=models.IntegerField(default=1800)
	array=models.CharField(max_length=1000,blank=True,null=True)
	ans_array=models.CharField(max_length=1000,blank=True,null=True)
	flag=models.IntegerField(default=0)
	correct_count=models.IntegerField(default=0)
	percent=models.IntegerField(default=0)	
	percent_flag=models.IntegerField(default=0)
	
	def __str__(self):
		return  self.user1

class Senior(models.Model):
	user1=models.CharField(max_length=15)
	user2=models.CharField(max_length=15)
	college=models.CharField(max_length=20)
	phone=models.CharField(max_length=12)
	email=models.EmailField(max_length=50,unique=True)
	password=models.CharField(max_length=25)
	score=models.IntegerField(default=0)
	logintime=models.IntegerField(default=0)
	timestamp=models.IntegerField(default=1800)
	array=models.CharField(max_length=1000,blank=True,null=True)
	ans_array=models.CharField(max_length=1000,blank=True,null=True)
	flag=models.IntegerField(default=0)
	correct_count=models.IntegerField(default=0)
	percent=models.IntegerField(default=0)
	percent_flag=models.IntegerField(default=0)
	def __str__(self):
		return  self.user1

class jquestions(models.Model):
	qid=models.IntegerField(unique=True)
	question=models.CharField(max_length=1000)
	op1=models.CharField(max_length=1000)
	op2=models.CharField(max_length=1000)
	op3=models.CharField(max_length=1000)
	op4=models.CharField(max_length=1000)
	ans=models.CharField(max_length=5)

	def __str__(self):
		return str(self.qid)

class squestions(models.Model):
	qid=models.IntegerField(unique=True)
	question=models.CharField(max_length=1000)
	op1=models.CharField(max_length=1000)
	op2=models.CharField(max_length=1000)
	op3=models.CharField(max_length=1000)
	op4=models.CharField(max_length=1000)
	ans=models.CharField(max_length=5)

	def __str__(self):
		return str(self.qid)
