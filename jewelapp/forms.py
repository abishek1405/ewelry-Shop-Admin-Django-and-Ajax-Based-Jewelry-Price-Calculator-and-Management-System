
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Lecturer,Student,Seldealer
from django.contrib.auth.models import User as U
from django.db import transaction


# Create your models here.


class Dealerform(forms.Form):
    name                = forms.CharField(label="name",max_length=1000)
    store_name          = forms.CharField(label="store_name",max_length=1000)
    contact             = forms.CharField(label="contact",max_length=2000)
    product_name        = forms.CharField(label="product_name",max_length=1000)
    type_of_product     = forms.CharField(label="type_of_product",max_length=2000)
    created_at          = forms.CharField(label='created_at',max_length=60)
    product_quality     = forms.CharField(label="product_quality",max_length=1000)
    precious_metal      = forms.CharField(label="precious_metal ",max_length=10)
    percent             = forms.CharField(label="percent",max_length=10000)
    pure_rate           = forms.CharField(label="pure_rate",max_length=10000)
    percent           = forms.CharField(label="percent",max_length=30)

class seldealerforms(forms.Form):
    sname            = forms.CharField(label='sname',max_length=1000)
    sstore_name      = forms.CharField(label='sstore_name',max_length=1000)
    scommuni         = forms.CharField(label='scommuni',max_length=2000)
    sproduct_name    = forms.CharField(label='sproduct_name',max_length=1000)
    stype_of_product = forms.CharField(label='stype_of_product',max_length=2000)




class LecturerAddForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs = {'class':'form-control'}),label='Username',)
    address = forms.CharField(max_length=30,widget=forms.TextInput(attrs = {'class':'form-control'}),label="Address")
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}),label='Mobile No')
    firstname = forms.CharField(max_length=30,widget=forms.TextInput(attrs = {'class':'form-control'}),label="Firstname")
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Lastname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Email")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_lecturer = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        # if commit:
        #     user.save()
        # return user
        lecturer = Lecturer.objects.create(user=user, id_number=user.username)
        lecturer.save()
        return lecturer

class StudentAddForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs = {'class':'form-control'}),label='Username',)
    Address = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label='Address')
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label='Mobile No')
    firstname = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Firstname")
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Lastname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Email")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(user=user,id_number=user.username)
        student.save()
        return student
