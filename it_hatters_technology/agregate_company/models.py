from django.db import models
from django.contrib.postgres.fields import ArrayField

class Status(models.Model):
    name = models.CharField(max_length=64)

class Technologies(models.Model):
    name = models.CharField(max_length=32)

class Project(models.Model):
    name = models.CharField(max_length=32)
    workload = models.PositiveSmallIntegerField()
    deadline = models.DateField()
    technologies = ArrayField(models.CharField(max_length=32))

class Cityes(models.Model):
    name = models.CharField(max_length=64,unique=True)
class Grades(models.Model):
    grade_name = models.CharField(max_length=16)


class Employee(models.Model):
    first_name = models.CharField(max_length=20,blank=False,null=False)
    last_name = models.CharField(max_length=20,blank=False,null=False)
    patronymic = models.CharField(max_length=20, blank=True, null=True)  # Отчество
    hash_id = models.BigIntegerField(null=True)
    t_shirt_size = models.SmallIntegerField(null=True)
    shoe_size = models.SmallIntegerField(null=True)
    email = models.EmailField(null=True,default=None)
    phone_number = models.CharField(max_length=16,unique=True)
    role = models.CharField(max_length=64,default=None,null=True)
    position = models.CharField(max_length=64,default=None,null=True)
    status = models.ForeignKey(Status,on_delete=models.SET_NULL,null=True,default=None)
    path = models.FilePathField()
    about = models.TextField(null=True)
    work_project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,default=None)
    location = models.ForeignKey(Cityes,on_delete=models.SET_NULL,null=True,default=None)
    grade = models.ForeignKey(Grades,on_delete=models.SET_NULL,null=True,default=None)
    time_zone = models.CharField(max_length=10,null=True)
    skills = ArrayField(models.CharField(max_length=30),null=True)
    stack_technologies = ArrayField(models.CharField(max_length=20),null=True)
    address = models.CharField(max_length=128,null=True)

class Specializations(models.Model):
    name = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    experience = models.SmallIntegerField()

class Node(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64,null=True,default=None)