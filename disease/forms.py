from django.forms import ModelForm
from .models import Diseasetype,Country,Disease,Discover,Users,Publicservant,Doctor,Specialize,Record

from django.contrib.auth.forms import UsernameField

from django import forms



class DiseasetypeForm(ModelForm):
    class Meta:
        model = Diseasetype
        fields = ('id','description')
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control', 'autofocus': True}),
            'description': forms.TextInput(attrs={'class': 'input', 'required': True}),
        }

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ('cname','population')
        widgets = {
            'cname': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            'population': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
        }

class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = ('disease_code','pathogen','description','id')
        widgets = {
            'disease_code': forms.TextInput(attrs={'class': 'input', 'autofocus': True}),
            'pathogen': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'id': forms.Select(attrs={'class': 'input', 'required': True}),

        }

class DiscoverForm(ModelForm):
    class Meta:
        model = Discover
        fields = ('cname','disease_code','first_enc_date')
        widgets = {
            'cname': forms.Select(attrs={'class': 'input', 'autofocus': True}),
            'disease_code': forms.Select(attrs={'class': 'input', 'required': True}),
            'first_enc_date': forms.DateInput(attrs={'class': 'input', 'required': True}),


        }


class UsersForm(ModelForm):

    class Meta:
        model = Users
        fields = ('email','name','surname','salary','phone','cname')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input', 'autofocus': True}),
            'name': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'surname': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'salary': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'input', 'required': True}),
            'cname': forms.Select(attrs={'class': 'input', 'required': True}),
        }


class PublicServantForm(ModelForm):
    class Meta:
        model = Publicservant
        fields = ('email','department')
        widgets = {
            'email': forms.Select(attrs={'class': 'input', 'autofocus': True}),
            'department': forms.TextInput(attrs={'class': 'input', 'required': True}),

        }

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('email','degree')
        degree = [
            ('Bachelor', 'Bachelor'),
            ('MD', 'MD'),
            ('PhD', 'PhD'),
            ('Doctoral', 'Doctoral'),

        ]
        widgets = {
            'email': forms.Select(attrs={'class': 'input', 'autofocus': True}),
            'degree': forms.Select(attrs={'class': 'input', 'required': True}),

        }


class SpecializeForm(ModelForm):
    class Meta:
        model = Specialize
        fields = ('sid','email')
        widgets = {
            'sid': forms.Select(attrs={'class': 'input', 'autofocus': True}),
            'email': forms.Select(attrs={'class': 'input', 'required': True}),

        }

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ('email','cname','disease_code','total_deaths','total_patients')
        widgets = {
            'email': forms.Select(attrs={'class': 'input', 'autofocus': True}),
            'cname': forms.Select(attrs={'class': 'input', 'required': True}),
            'disease_code': forms.Select(attrs={'class': 'input', 'required': True}),
            'total_deaths': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'total_patients': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
        }

