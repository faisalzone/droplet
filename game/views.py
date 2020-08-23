from django.shortcuts import render, redirect

# Create your views here.
from task.models import Day, Task


def start_game(request):
    return render(request, 'game/start.html')


def day_one_task_one(request):
    task1 = Task.objects.get(seq=1)
    task1.completed_day_one = False
    task1.completed_day_two = False
    task1.completed_day_three = False
    task1.completed_day_four = False
    task1.completed_day_five = False
    task1.completed_day_six = False
    task1.completed_day_seven = False
    task1.save()
    task2 = Task.objects.get(seq=2)
    task2.completed_day_one = False
    task2.completed_day_two = False
    task2.completed_day_three = False
    task2.completed_day_four = False
    task2.completed_day_five = False
    task2.completed_day_six = False
    task2.completed_day_seven = False
    task2.save()
    task3 = Task.objects.get(seq=3)
    task3.completed_day_one = False
    task3.completed_day_two = False
    task3.completed_day_three = False
    task3.completed_day_four = False
    task3.completed_day_five = False
    task3.completed_day_six = False
    task3.completed_day_seven = False
    task3.save()
    task4 = Task.objects.get(seq=4)
    task4.completed_day_one = False
    task4.completed_day_two = False
    task4.completed_day_three = False
    task4.completed_day_four = False
    task4.completed_day_five = False
    task4.completed_day_six = False
    task4.completed_day_seven = False
    task4.save()
    task5 = Task.objects.get(seq=5)
    task5.completed_day_one = False
    task5.completed_day_two = False
    task5.completed_day_three = False
    task5.completed_day_four = False
    task5.completed_day_five = False
    task5.completed_day_six = False
    task5.completed_day_seven = False
    task5.save()
    task6 = Task.objects.get(seq=6)
    task6.completed_day_one = False
    task6.completed_day_two = False
    task6.completed_day_three = False
    task6.completed_day_four = False
    task6.completed_day_five = False
    task6.completed_day_six = False
    task6.completed_day_seven = False
    task6.save()
    task7 = Task.objects.get(seq=7)
    task7.completed_day_one = False
    task7.completed_day_two = False
    task7.completed_day_three = False
    task7.completed_day_four = False
    task7.completed_day_five = False
    task7.completed_day_six = False
    task7.completed_day_seven = False
    task7.save()
    request.session['total_litre'] = 100
    remaining_water = request.session.get('total_litre')
    request.session['remaining_water'] = remaining_water
    day = Day.objects.get(number=1)
    task = Task.objects.get(seq=1)
    tasks = Task.objects.all()
    context = {
        'day': day,
        'task': task,
        'tasks': tasks,
        'remaining_water': remaining_water,
    }
    return render(request, 'game/day-one/task-1.html', context)


def day_one_task_one_yes(request):
    task = Task.objects.get(seq=1)
    remaining_water = request.session.get('remaining_water')
    new_remaining_water = int(remaining_water) - int(task.water_qty)
    request.session['remaining_water'] = new_remaining_water
    task.completed_day_one = True
    task.save()
    return redirect('game:day_one_task_two')


def day_one_task_two(request):
    remaining_water = request.session.get('remaining_water')
    day = Day.objects.get(number=1)
    task = Task.objects.get(seq=2)
    tasks = Task.objects.all()
    context = {
        'day': day,
        'task': task,
        'tasks': tasks,
        'remaining_water': remaining_water,
    }
    return render(request, 'game/day-one/task-2.html', context)


def day_one_task_three(request):
    day = Day.objects.get(number=1)
    tasks = Task.objects.all()
    context = {
        'day': day,
        'tasks': tasks,
    }
    return render(request, 'game/day-one/task-1.html', context)


def day_one_task_four(request):
    day = Day.objects.get(number=1)
    tasks = Task.objects.all()
    context = {
        'day': day,
        'tasks': tasks,
    }
    return render(request, 'game/day-one/task-1.html', context)


def day_one_task_five(request):
    day = Day.objects.get(number=1)
    tasks = Task.objects.all()
    context = {
        'day': day,
        'tasks': tasks,
    }
    return render(request, 'game/day-one/task-1.html', context)


def day_one_task_six(request):
    day = Day.objects.get(number=1)
    tasks = Task.objects.all()
    context = {
        'day': day,
        'tasks': tasks,
    }
    return render(request, 'game/day-one/task-1.html', context)


def day_one_task_seven(request):
    day = Day.objects.get(number=1)
    tasks = Task.objects.all()
    context = {
        'day': day,
        'tasks': tasks,
    }
    return render(request, 'game/day-one/task-1.html', context)
