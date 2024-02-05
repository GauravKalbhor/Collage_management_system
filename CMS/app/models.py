from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    adminID = models.CharField(max_length=50)
    adminPassword = models.CharField(max_length=50)

class Stu_FormDetails(models.Model):
    stu_ID = models.CharField(max_length=100)
    stu_Name = models.CharField(max_length=100)
    stu_DOB = models.DateField(auto_now=True)
    stu_Email = models.EmailField(max_length=100)
    stu_Mobile = models.IntegerField(max_length=99999999999)
    stu_Gender = models.CharField(max_length=10)
    stu_Department = models.CharField(max_length=50)
    stu_Course = models.CharField(max_length=50)

class Teach_FormDetails(models.Model):
    teach_ID = models.CharField(max_length=100)
    teach_jtitle = models.CharField(max_length=100)
    teach_Name = models.CharField(max_length=100)
    teach_DOB = models.DateField(auto_now=True)
    teach_Email = models.EmailField(max_length=100)
    teach_Mobile = models.IntegerField(max_length=99999999999)
    teach_Gender = models.CharField(max_length=10)
    teach_Course = models.CharField(max_length=50)
    