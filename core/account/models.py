from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
# Create your models here.

    



class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    student_id=models.CharField(max_length=30,null=True,blank=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    Phone_number=models.CharField(max_length=10,null=True,blank=True)
    email=models.EmailField( max_length=254,null=True,blank=True)
    
class Document(models.Model):
    ch=[   ("ID","ID"),
        ("Certi","CERTIFICATE")]
    Document_name=models.CharField(max_length=30,null=True, blank=True)
    Document_no=models.CharField(max_length=30,null=True, blank=True)
    Document_type=models.CharField(max_length=30, choices= ch)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    Doc=models.ImageField(upload_to="documnet")