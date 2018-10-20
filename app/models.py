from django.db import models

# Create your models here.


class Grade(models.Model):
    g_name = models.CharField(max_length=50)
    g_num = models.PositiveIntegerField(default=40)

    def __str__(self):
        return self.g_name



class Student(models.Model):
    s_name = models.CharField(max_length=50)
    s_sex = models.BooleanField(default=True)
    s_grade = models.ForeignKey(Grade)

    def __str__(self):
        return self.s_name