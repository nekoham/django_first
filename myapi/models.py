from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=40)
    grade = models.FloatField()
    startDate = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.fName + " " + self.lName + " - Grade: " + str(self.grade)