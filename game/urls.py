from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('start/', views.start_game, name='start_game'),
    path('start/day-1/task-1/', views.day_one_task_one, name='day_one_task_one'),
    path('start/day-1/task-1/yes/', views.day_one_task_one_yes, name='day_one_task_one_yes'),
    path('start/day-1/task-2/', views.day_one_task_two, name='day_one_task_two'),
]
