from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from dateutil.parser import parse
import datetime
# Create your models here.

class Dealer(models.Model):
    name            = models.CharField(max_length=1000)
    store_name      = models.CharField(max_length=1000)
    contact         = models.CharField(max_length=2000)
    product_name     = models.CharField(max_length=1000)
    type_of_product   = models.CharField(max_length=2000)
    created_at        = models.CharField(max_length=50)
    product_quality    = models.CharField(max_length=1000)
    precious_metal      = models.CharField(max_length=10)
    discount             = models.CharField(max_length=10000)
    percent         = models.CharField(max_length=30)
    pure_rate           = models.CharField(max_length=10000)



class Seldealer(models.Model):
    sname            = models.CharField(max_length=1000)
    sstore_name      = models.CharField(max_length=1000)
    scommuni         = models.CharField(max_length=2000)
    sproduct_name     = models.CharField(max_length=1000)
    stype_of_product   = models.CharField(max_length=2000)
    
        

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    phone = models.CharField(max_length=60,blank=True, null=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.CharField(max_length=255)

    def __str__(self):
        return self.id_number
    # def get_absolute_url(self):
    #     return reverse('profile')
class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=255)

    def __str__(self):
        return self.id_number

    # def get_absolute_url(self):
    #     return reverse('profile')
class CourseALlocation(models.Model):
    lecturer = models.ForeignKey(User,on_delete=models.CASCADE)



    