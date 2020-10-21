from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context={}
	return render(request,"MDShop/base.html",context)


def index(request):
	context={}
	return render(request,"MDShop/index.html",context)



def Post(request):
	context={}
	return render(request,"MDShop/main.html",context)