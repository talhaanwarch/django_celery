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
		task_id= perform_task.delay(input_text)
		context = {'output_text':task_id}
	else:
		context = {}
	return render(request,'home.html',context)