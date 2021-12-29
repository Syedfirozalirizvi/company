from django.shortcuts import get_object_or_404, render,redirect
from .forms import EmployeeForm , ProjectForm , ManagerField
from .models import Employee , Project , Manager
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views import generic
from django.views.generic.edit import CreateView  
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.views.generic.edit import UpdateView
@method_decorator(login_required,name='dispatch')
class Home(View):
    
    def get(self,request, *args, **kwargs):
        
        
        return render(request, 'index.html')
@method_decorator(login_required,name='dispatch')
class CreateEmployee(CreateView):
    template_name = 'employee/create.html'
    form_class = EmployeeForm
    
    def get_success_url(self):
        return reverse('employee_list')
    
@method_decorator(login_required,name='dispatch')
class EmployeeList(generic.ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee/list.html'
    
@method_decorator(login_required,name='dispatch')
class EmployeeDelete(DeleteView):
    
    model = Employee
    context_object_name = 'employees'
    
    
    def get_success_url(self):
        return reverse('employee_list')
        
@method_decorator(login_required,name='dispatch')    
class UpdataEmployee(UpdateView):
    
    model = Employee
    fields = '__all__'
    template_name = 'employee/update.html'
    
    def get_success_url(self):
        return reverse('employee_list')
    

@method_decorator(login_required,name='dispatch')
class CreateProject(CreateView):
    
    template_name = 'project/create.html'
    form_class = ProjectForm
    
    def get_success_url(self):
        return reverse('project_list')

@method_decorator(login_required,name='dispatch')
class ProjectList(generic.ListView):
    
    model = Project
    context_object_name = 'projects'
    template_name = 'project/list.html'
        
        
@method_decorator(login_required,name='dispatch')
class ProjectDelete(DeleteView):
    
    model = Project
    context_object_name = 'projects'
    
    def get_success_url(self):
        return reverse('project_list')
        
        
@method_decorator(login_required,name='dispatch')
class UpdateProject(UpdateView):
    
   model = Project
   fields ='__all__'
   template_name = 'project/update.html'
   
   def get_success_url(self):
        return reverse('project_list')
    
    
@method_decorator(login_required,name='dispatch')
class CreateManager(CreateView):
    
    template_name = 'manager/create.html'
    form_class = ManagerField
    
    def get_success_url(self):
        return reverse('manager_list')

        
@method_decorator(login_required,name='get')
class ManagerList(generic.ListView):
    model = Manager
    context_object_name = 'managers'
    template_name = 'manager/list.html'
        
@method_decorator(login_required,name='dispatch')
class ManagerDelete(DeleteView):
    
    model = Manager
    context_object_name = 'managers'
        
    def get_success_url(self):
        return reverse('manager_list')
@method_decorator(login_required,name='dispatch')    
class UpdateManager(UpdateView):
    
    model = Manager
    fields = '__all__'
    template_name = 'manager/update.html'
    
    def get_success_url(self):
        return reverse('manager_list')
    

        
