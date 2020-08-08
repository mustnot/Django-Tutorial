from django.db import models
from django.utils import timezone


class Activity(models.Model):
    f5_date = models.DateField()
    act_title = models.TextField()
    act_time = models.TimeField(default="00:00:00")

    founder = models.CharField(max_length=10)
    location = models.TextField()

    minimum = models.IntegerField(default=1)
    maximum = models.IntegerField(default=5)

    def __str__(self):
        return self.act_title
        
    def is_over_date(self):
        return timezone.now() <= self.f5_date

    def is_register_possible(self):
        participants_number = len(Participants.objects.filter(activity=self))
        print(participants_number)
        return self.maximum > participants_number


class Participants(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=10)
    def __str__(self):
        return self.emp_id
