# Generated by Django 3.1 on 2020-08-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='task.Task'),
        ),
    ]