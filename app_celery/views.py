from django.shortcuts import render
def home(request):
	return render(request,'home.html',{'print':"every thing ok"})