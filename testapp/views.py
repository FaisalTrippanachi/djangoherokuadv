from django.shortcuts import render
from django.http import HttpResponse

# Create your views h
def home(request):
	return render(request,'home.html')

def test(request):
	return render(request,'test.html')


def test2(request):
	return render(request,'fn/test2.html')
