# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Owner
from django.http import HttpResponse

def testdb(request):
	owner=Owner(ownerName='zqw')
	owner.save()
	return render(request, 'Model/test.html')