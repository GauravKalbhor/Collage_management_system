from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    adminID = models.CharField(max_length=50)
    adminPassword = models.CharField(max_length=50)

class Stu_Details(models.Model):
    stu_FistName = models.CharField(max_length=100)
    stu_LastName = models.CharField(max_length=100)
    stu_RollNo = models.CharField(max_length=100)
    stu_Email = models.EmailField()
    stu_Contact = models.IntegerField()
    stu_Fee = models.IntegerField()
    stu_Course = models.CharField(max_length=100)
    stu_Branch = models.CharField(max_length=100)
    stu_Year = models.IntegerField()