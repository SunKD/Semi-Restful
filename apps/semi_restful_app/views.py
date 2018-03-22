# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, 'semi_restful_app/index.html', {"users": User.objects.all()})

def show(request, id):
    return render(request, 'semi_restful_app/show.html', {"user": User.objects.get(id= id)})

def new(request):
    return render(request, 'semi_restful_app/new.html')

def edit(request, id):
    return render(request, 'semi_restful_app/edit.html', {"user": User.objects.get(id= id)})

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/new')
    else:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        User.objects.create(first_name=fname, last_name=lname, email=email)
        return redirect('/')

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/edit/' + str(id))
    else:
        edituser = User.objects.get(id=id)
        fname=request.POST['first_name']
        lname = request.POST['last_name']
        edituser.first_name = fname
        edituser.last_name = lname
        edituser.email = request.POST['email']
        edituser.save()
        userid=edituser.id
        return redirect('/show/'+str(userid))

