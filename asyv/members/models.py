from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    gender = models.CharField (null=True, blank=True, max_length=50)
    age = models.IntegerField(null=True, blank=True)
    grade = models.CharField(null=True, blank=True, max_length=50)
    date = models.DateTimeField(null=True, blank=True, max_length=50)
    family = models.CharField(null=True, blank=True, max_length=50)
    nurse = models.CharField(max_length=50, blank=True)
    medecine = models.CharField(max_length=500, blank=True, null=True)
    details = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.first_name
    
class Meal(models.Model):
    names = models.CharField(null=True, blank=True, max_length=50)
    meals = models.CharField(null=True, blank=True, max_length=50)
    received_date = models.DateTimeField(null=True, blank=True, max_length=50)
    expired_date = models.DateField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.meals
    
class School(models.Model):
    names = models.CharField(null=True, blank=True, max_length=50)
    grade = models.CharField(null=True, blank=True, max_length=50)
    date = models.DateField(null=True, blank=True, max_length=50)
    reason = models.CharField(null=True, blank=True, max_length=50)
    special_issues = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.names
