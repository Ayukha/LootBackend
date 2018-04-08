# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile:
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	zeal_id = models.CharField(max_length=10, blank=True)


class level:
	bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    question = models.CharField(max_length=30, blank=True)
    answer = models.CharField(max_length=30, blank=True)