from django.shortcuts import render  # Import for rendering Django templates
from time import sleep             # Import for simulating a time-consuming task
from celery import shared_task     # Import for defining Celery tasks
from celery.result import AsyncResult  # Import for checking task status
from project_celery.celery import app  # Import the Celery app instance
from django.http import JsonResponse  # Import for returning JSON responses


@shared_task()  # Decorate a function as a Celery task
def perform_task(input_text):
    sleep(10)  # Simulate a 10-second task duration
    return input_text  # Return the input text as the result


def home(request):
    if request.method == 'POST':
        input_text = request.POST['input']  # Get input text from the POST request
        task_id = perform_task.delay(input_text)  # Asynchronously call the task
        context = {'output_text': str(task_id)}  # Prepare a context for the response
        return JsonResponse(context)  # Return a JSON response with the task ID
    else:
        context = {}  # Provide an empty context for a GET request
    return render(request, 'home.html', context)  # Render the home template


def check_task_result(request, task_id):
    result = AsyncResult(task_id, app=app)  # Get the task result object
    while True:
        if result.state == 'SUCCESS':
            print('state', result.state)
            output = result.get()  # Retrieve the task output
            return JsonResponse({'task_id': task_id, 'status': result.state, 'output': output})
        else:
            print('state', result.state)
            return JsonResponse({'task_id': task_id, 'status': result.state}, status=202)  # 202 Accepted

