from django.db import models


class Teacher_Data(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)

    class Meta:
        app_label = 'teacher'

    def __str__(self):
        return self.name