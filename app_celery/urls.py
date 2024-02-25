from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('check_task_result/<str:task_id>/',views.check_task_result,name='check_task_result'),
    # this path will take task_id as a parameter and pass it to the check_task_result function
    ]