from django import forms
from .models import *


class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(EmployeeForm, self).__init__(*args, **kwargs)
       self.fields['first_name'].widget.attrs['readonly'] = True
       self.fields['last_name'].widget.attrs['readonly'] = True
       self.fields['email'].widget.attrs['readonly'] = True

    
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