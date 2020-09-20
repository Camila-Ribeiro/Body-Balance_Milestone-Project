from django.db import models


class Workouts(models.Model):

    class Meta:
        verbose_name_plural = 'workouts'

    current_week = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    main_goal = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=100)
    training_level = models.CharField(max_length=100)
    program_duration = models.CharField(max_length=100)
    days_per_week = models.IntegerField(blank=True, null=True)
    time_per_workout = models.CharField(max_length=100)
    equipments_required = models.TextField(max_length=1000)
    author_name = models.CharField(max_length=100)

