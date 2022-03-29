from django.db import models
from teacher.models import Teacher_Data


class Student_Data(models.Model):
    name = models.CharField(max_length=122)
    roll = models.IntegerField()
    city = models.CharField(max_length=122)

    class Meta:
        app_label = 'student'

    def __str__(self):
        return self.name


