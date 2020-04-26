from django.shortcuts import render
from django.http import HttpResponse

# Create your views h
def home(request):
	return render(request,'home.html')
