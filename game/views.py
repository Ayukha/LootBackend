# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from models import *
import requests
from django.shortcuts import get_object_or_404
# from game.forms import SignUpForm

# Create your views here.
@login_required
def home(request):
	"""For Home Page Display"""
	return render()



@login_required
def description(request):
	""" profile editing view. User can update their profile using this view. """
	if request.user.is_authenticated():
		return render_to_response("description.html")
	else:
		return HttpResponseRedirect()


@login_required
def mystery(request , id):

	current_profile =profile.objects.get(id=request.user.id)
	print(current_profile.current_level)
	print(id)
	if int(current_profile.current_level) == int(id):
		# print("first")
		levels = level.objects.get(id=id)
		if request.method == "GET":
			# bio = level.objects.get(pk=1)
			context = {
				'bio': levels.bio
			}
			return render(request,'game/mystery.html',context)
		elif request.method == "POST":
			
			r = requests.post(
				'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBInKir6vNuHLnNkz-PJZa6nW5SqFZfJho'
				)
			location = r.json()
			print(location['location']['lat'])
			print("in else")
			# print(levels.id)
			print(levels.location)
			# if 
			if str(location['location']['lat']) == str(levels.location):
				print(levels.question)
				current_profile.current_level = int(id)+int(1)
				current_profile.save(update_fields=["current_level"])
			# levels = level.objects.get(id=id)
				return HttpResponse(levels.question)
			else:
				return HttpResponseRedirect('/mystery/'+id)
		# # return HttpResponse(levels.location)
	
	else:
		return HttpResponse("404")

			# return HttpResponse(location['location']['lat'])
	# if request.user.is_authenticated():
	# 	user = Profile.objects.get(Zealid = request.user.username)


