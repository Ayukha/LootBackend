# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class level(models.Model):
	user = models.ForeignKey(User)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	question = models.CharField(max_length=30, blank=True)
	answer = models.CharField(max_length=30, blank=True)



class profile(models.Model):

	current_level = models.IntegerField(default=1)