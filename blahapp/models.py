# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.



class Cat(models.Model):
	name = models.CharField(max_length=200)
	owner = models.ForeignKey('blahapp.Human')
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Cat: " + self.name

class Human(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return "Human: " + self.name



