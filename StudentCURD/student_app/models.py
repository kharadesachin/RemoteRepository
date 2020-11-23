from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    marathi_marks = models.IntegerField()
    english_marks = models.IntegerField()
    hindi_marks = models.IntegerField()
    maths_marks  = models.IntegerField()
    science_marks = models.IntegerField()
    social_marks = models.IntegerField()
