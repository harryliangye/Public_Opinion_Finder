from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
def home(request):
	return render(request,'Home/home.html')

def Author(request):
	return render(request,'Home/Author.html')

def UnderConstruction(request):
	return HttpResponse("Sorry, This module is UnderConstruction, It will be release soon........")