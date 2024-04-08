
from django import forms
from jobapp.models import Employee,Position

class Employee_ModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fullname','mobile','emp_code','position']

        labels = {
            "fullname" : "Full Name",
            'emp_code' : "EMP.CODE",
        }


class Position_ModelForm(forms.ModelForm):
    class Meta:
        model = Position
        # fields = '__all__'
        fields = ['title']

        labels = {
            "title" : "Add title"
        }