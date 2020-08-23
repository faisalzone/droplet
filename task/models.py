from django.db import models

# Create your models here.
class Task(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=70)
    question = models.CharField(max_length=250, blank=True)
    completed_day_one = models.BooleanField(default=False)
    completed_day_two = models.BooleanField(default=False)
    completed_day_three = models.BooleanField(default=False)
    completed_day_four = models.BooleanField(default=False)
    completed_day_five = models.BooleanField(default=False)
    completed_day_six = models.BooleanField(default=False)
    completed_day_seven = models.BooleanField(default=False)
    water_qty = models.IntegerField()

    def __str__(self):
        return str(self.title)


class Day(models.Model):
    number = models.IntegerField()
    tasks = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return str(self.number)
