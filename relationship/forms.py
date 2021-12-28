from django import forms
from .models import *


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields ="__all__"
        
        
class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields ='__all__'
        
class ManagerField(forms.ModelForm):
    
    class Meta:
        model = Manager
        fields ='__all__'