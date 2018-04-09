# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from game.forms import SignUpForm

# Create your views here.

def home(request):
	"""For Home Page Display"""

	if request.user.is_authenticated():
		return render()



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
	""" Login view """
	if not request.user.is_authenticated():
		if request.POST:
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				# Correct password, and the user is marked "active"
				auth.login(request,user)
				# Redirect to a success page.
				return HttpResponseRedirect("/description")
			else:
				# Show an error page
				return render_to_response("login.html",{"error":1},context_instance = RequestContext(request))
		return render_to_response('login.html',context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/mystery")



def description(request):
	""" profile editing view. User can update their profile using this view. """
	if request.user.is_authenticated():
		return render_to_response("description.html")
	else:
		return HttpResponseRedirect()


def mystery(request):
	if request.method == "GET":
		return render(request,'game/mystery.html')
	if request.method == "POST":
		print("in else")
		return HttpResponse('dfbdxfb')
	if request.user.is_authenticated():
		user = Profile.objects.get(Zealid = request.user.username)


