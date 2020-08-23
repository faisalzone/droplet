from django.contrib import admin
from .models import Task, Day


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = ['seq', 'title', 'question', 'water_qty', 'completed_day_one', 'completed_day_two', 'completed_day_three', 'completed_day_four', 'completed_day_five', 'completed_day_six', 'completed_day_seven']
    list_display = ['seq', 'title', 'water_qty']
    list_filter = ['water_qty']
    search_fields = ['title']


class DayAdmin(admin.ModelAdmin):
    fields = ['number', 'tasks']
    list_display = ['number']


admin.site.register(Task, TaskAdmin)
admin.site.register(Day, DayAdmin)
