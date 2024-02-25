from django.shortcuts import render
from time import sleep
from celery import shared_task

@shared_task()
def perform_task(input_text):
	sleep(60)
	return input_text

def home(request):
	if request.method == 'POST':
		input_text = request.POST['input']
		input_text= perform_task.delay(input_text)
		context = {'output_text':input_text}
	else:
		context = {}
	return render(request,'home.html',context)