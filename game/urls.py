from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('start/', views.start_game, name='start_game'),
    # Day one tasks
    path('day-1/task-1/', views.day_one_task_one, name='day_one_task_one'),
    path('day-1/task-1/yes/', views.day_one_task_one_yes, name='day_one_task_one_yes'),
    path('day-1/task-2/', views.day_one_task_two, name='day_one_task_two'),
    path('day-1/task-2/yes/', views.day_one_task_two_yes, name='day_one_task_two_yes'),
    path('day-1/task-3/', views.day_one_task_three, name='day_one_task_three'),
    path('day-1/task-3/yes/', views.day_one_task_three_yes, name='day_one_task_three_yes'),
    path('day-1/task-4/', views.day_one_task_four, name='day_one_task_four'),
    path('day-1/task-4/yes/', views.day_one_task_four_yes, name='day_one_task_four_yes'),
    path('day-1/task-5/', views.day_one_task_five, name='day_one_task_five'),
    path('day-1/task-5/yes/', views.day_one_task_five_yes, name='day_one_task_five_yes'),
    path('day-1/task-6/', views.day_one_task_six, name='day_one_task_six'),
    path('day-1/task-6/yes/', views.day_one_task_six_yes, name='day_one_task_six_yes'),
    path('day-1/task-7/', views.day_one_task_seven, name='day_one_task_seven'),
    path('day-1/task-7/yes/', views.day_one_task_seven_yes, name='day_one_task_seven_yes'),

    # Day two tasks
    path('day-2/task-1/', views.day_two_task_one, name='day_two_task_one'),
    path('day-2/task-1/yes/', views.day_two_task_one_yes, name='day_two_task_one_yes'),
    path('day-2/task-2/', views.day_two_task_two, name='day_two_task_two'),
    path('day-2/task-2/yes/', views.day_two_task_two_yes, name='day_two_task_two_yes'),
    path('day-2/task-3/', views.day_two_task_three, name='day_two_task_three'),
    path('day-2/task-3/yes/', views.day_two_task_three_yes, name='day_two_task_three_yes'),
    path('day-2/task-4/', views.day_two_task_four, name='day_two_task_four'),
    path('day-2/task-4/yes/', views.day_two_task_four_yes, name='day_two_task_four_yes'),
    path('day-2/task-5/', views.day_two_task_five, name='day_two_task_five'),
    path('day-2/task-5/yes/', views.day_two_task_five_yes, name='day_two_task_five_yes'),
    path('day-2/task-6/', views.day_two_task_six, name='day_two_task_six'),
    path('day-2/task-6/yes/', views.day_two_task_six_yes, name='day_two_task_six_yes'),
    path('day-2/task-7/', views.day_two_task_seven, name='day_two_task_seven'),
    path('day-2/task-7/yes/', views.day_two_task_seven_yes, name='day_two_task_seven_yes'),

    # # Day three tasks
    # path('day-3/task-1/', views.day_three_task_one, name='day_three_task_one'),
    # path('day-3/task-1/yes/', views.day_three_task_one_yes, name='day_three_task_one_yes'),
    # path('day-3/task-2/', views.day_three_task_two, name='day_three_task_two'),
    # path('day-3/task-2/yes/', views.day_three_task_two_yes, name='day_three_task_two_yes'),
    # path('day-3/task-3/', views.day_three_task_three, name='day_three_task_three'),
    # path('day-3/task-3/yes/', views.day_three_task_three_yes, name='day_three_task_three_yes'),
    # path('day-3/task-4/', views.day_three_task_four, name='day_three_task_four'),
    # path('day-3/task-4/yes/', views.day_three_task_four_yes, name='day_three_task_four_yes'),
    # path('day-3/task-5/', views.day_three_task_five, name='day_three_task_five'),
    # path('day-3/task-5/yes/', views.day_three_task_five_yes, name='day_three_task_five_yes'),
    # path('day-3/task-6/', views.day_three_task_six, name='day_three_task_six'),
    # path('day-3/task-6/yes/', views.day_three_task_six_yes, name='day_three_task_six_yes'),
    # path('day-3/task-7/', views.day_three_task_seven, name='day_three_task_seven'),
    # path('day-3/task-7/yes/', views.day_three_task_seven_yes, name='day_three_task_seven_yes'),
    #
    # # Day four tasks
    # path('day-4/task-1/', views.day_four_task_one, name='day_four_task_one'),
    # path('day-4/task-1/yes/', views.day_four_task_one_yes, name='day_four_task_one_yes'),
    # path('day-4/task-2/', views.day_four_task_two, name='day_four_task_two'),
    # path('day-4/task-2/yes/', views.day_four_task_two_yes, name='day_four_task_two_yes'),
    # path('day-4/task-3/', views.day_four_task_three, name='day_four_task_three'),
    # path('day-4/task-3/yes/', views.day_four_task_three_yes, name='day_four_task_three_yes'),
    # path('day-4/task-4/', views.day_four_task_four, name='day_four_task_four'),
    # path('day-4/task-4/yes/', views.day_four_task_four_yes, name='day_four_task_four_yes'),
    # path('day-4/task-5/', views.day_four_task_five, name='day_four_task_five'),
    # path('day-4/task-5/yes/', views.day_four_task_five_yes, name='day_four_task_five_yes'),
    # path('day-4/task-6/', views.day_four_task_six, name='day_four_task_six'),
    # path('day-4/task-6/yes/', views.day_four_task_six_yes, name='day_four_task_six_yes'),
    # path('day-4/task-7/', views.day_four_task_seven, name='day_four_task_seven'),
    # path('day-4/task-7/yes/', views.day_four_task_seven_yes, name='day_four_task_seven_yes'),
    #
    # # Day five tasks
    # path('day-5/task-1/', views.day_five_task_one, name='day_five_task_one'),
    # path('day-5/task-1/yes/', views.day_five_task_one_yes, name='day_five_task_one_yes'),
    # path('day-5/task-2/', views.day_five_task_two, name='day_five_task_two'),
    # path('day-5/task-2/yes/', views.day_five_task_two_yes, name='day_five_task_two_yes'),
    # path('day-5/task-3/', views.day_five_task_three, name='day_five_task_three'),
    # path('day-5/task-3/yes/', views.day_five_task_three_yes, name='day_five_task_three_yes'),
    # path('day-5/task-4/', views.day_four_five_four, name='day_five_task_four'),
    # path('day-5/task-4/yes/', views.day_five_task_four_yes, name='day_five_task_four_yes'),
    # path('day-5/task-5/', views.day_five_task_five, name='day_five_task_five'),
    # path('day-5/task-5/yes/', views.day_five_task_five_yes, name='day_five_task_five_yes'),
    # path('day-5/task-6/', views.day_five_task_six, name='day_five_task_six'),
    # path('day-5/task-6/yes/', views.day_five_task_six_yes, name='day_five_task_six_yes'),
    # path('day-5/task-7/', views.day_five_task_seven, name='day_five_task_seven'),
    # path('day-5/task-7/yes/', views.day_five_task_seven_yes, name='day_five_task_seven_yes'),
    #
    # # Day five tasks
    # path('day-6/task-1/', views.day_six_task_one, name='day_six_task_one'),
    #
    # # Day five tasks
    # path('day-7/task-1/', views.day_seven_task_one, name='day_seven_task_one'),

]
