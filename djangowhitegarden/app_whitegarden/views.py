from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/home_white.html')

def waterstorage_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/waterstorage_page.html')

def mdb_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/mdb_page.html')

def air_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/air_page.html')

def floor1_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/floor1_page.html')

def floor2_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/floor2_page.html')

def floor3_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/floor3_page.html')

def floor4_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/floor4_page.html')

def floor5_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/floor5_page.html')

def room_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/room_page.html')

def graph_air_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/graph_air_page.html')

def graph_room_page(request):
    #return HttpResponse('<h1>Hello Django</h1>') 
	return render(request,'whitegarden/graph_room_page.html')




