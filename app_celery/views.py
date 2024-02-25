from django.shortcuts import render
from time import sleep
def home(request):
	if request.method == 'POST':
		input_text = request.POST['input']
		sleep(60)
		context = {'output_text':input_text}
	else:
		context = {}
	return render(request,'home.html',context)