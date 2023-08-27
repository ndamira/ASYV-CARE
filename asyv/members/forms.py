from django import forms
from .models import Student, Meal, School
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class PatientForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'age', 'grade','date', 'family', 'nurse', 'medecine', 'details']

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data:
            raise forms.ValidationError("This field cannot be empty.")
        return data
        
class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['names', 'meals','received_date', 'expired_date']

    def clean_names(self):
        data = self.cleaned_data['names']
        if not data:
            raise forms.ValidationError("This field cannot be empty.")
        return data
        
class SchoolInfo(forms.ModelForm):
    class Meta:
        model = School
        fields = ['names', 'grade', 'date', 'reason', 'special_issues']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_names(self):
        data = self.cleaned_data['names']
        if not data:
            raise forms.ValidationError("This field cannot be empty.")
        return data
