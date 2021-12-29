from django.shortcuts import get_object_or_404, render,redirect
from .forms import EmployeeForm , ProjectForm , ManagerField
from .models import Employee , Project , Manager
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

@method_decorator(login_required,name='dispatch')
class Home(View):
    
    def get(self,request, *args, **kwargs):
        
        
        return render(request, 'index.html')
@method_decorator(login_required,name='dispatch')
class CreateEmployee(View):
    
        def post(self,request, *args, **kwargs):
            
            employee_form = EmployeeForm(request.POST)
            if employee_form.is_valid():
                employee_form.save()
                messages.success(request, 'Successfully Employee Created!')
                return redirect('employee_list')
            
        def get(self,request, *args, **kwargs):
            
            employee_form = EmployeeForm()
            return render(request,'employee/create.html',{'forms':employee_form})
@method_decorator(login_required,name='dispatch')
class EmployeeList(View):
    
    def get(self,request, *args, **kwargs):
        
        employee_list = Employee.objects.all()
        ctx = {'employees':employee_list}
        return render(request,'employee/list.html',ctx)
@method_decorator(login_required,name='dispatch')
class EmployeeDelelte(View):
    
    def get(self,request,id, *args, **kwargs):
        
        employee = Employee.objects.get(id=id).delete()
        messages.success(request, 'Employee Deleted!')
        return redirect('employee_list')
@method_decorator(login_required,name='dispatch')    
class UpdataEmployee(View):
    
    def get(self,request,id, *args, **kwargs):
        employee = get_object_or_404(Employee, id = id)
        
        employee_form = EmployeeForm(instance = employee)
        return render(request,'employee/update.html',{'forms':employee_form})
    
    def post(self,request,id, *args, **kwargs):
        employee = get_object_or_404(Employee, id = id)
        employee_form = EmployeeForm(request.POST or None, instance = employee)
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request, 'Successfully Employee Updated!')
            return redirect('employee_list')
    

@method_decorator(login_required,name='dispatch')
class CreateProject(View):
    
    def post(self,request, *args, **kwargs):

        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
        return redirect('project_list')
    
    def get(self,request, *args, **kwargs):
        project_form = ProjectForm()
        return render(request,'project/create.html',{'forms':project_form})

@method_decorator(login_required,name='dispatch')
class ProjectList(View):
    
    def get(self,request, *args, **kwargs):
        
        project_list = Project.objects.all()
        ptx = {'projects':project_list}
        return render(request,'project/list.html',ptx)
@method_decorator(login_required,name='dispatch')
class ProjectDelete(View):
    
    def get(self,request,id,*args, **kwargs):
        
        project = Project.objects.get(id=id).delete()
        messages.success(request, 'Project Deleted!')
        return redirect('project_list')
@method_decorator(login_required,name='dispatch')
class UpdateProject(View):
    
    def get(self,request,id,*args, **kwargs):
        
        project = get_object_or_404(Project,id=id)
        project_form = ProjectForm(instance = project)
        return render(request,'project/update.html',{'forms':project_form})
    
    def post(self,request,id, *args, **kwargs):
        
            project = get_object_or_404(Project,id=id)
            project_form = ProjectForm(request.POST or None, instance = project)
            if project_form.is_valid():
                project_form.save()
                messages.success(request, 'Successfully Employee Updated!')
                return redirect('project_list')
@method_decorator(login_required,name='dispatch')
class CreateManager(View):
    
    def post(self,request, *args, **kwargs):

        manager_form = ManagerField(request.POST)
        if manager_form.is_valid():
            manager_form.save()
        return redirect('manager_list')
    
    def get(self,request,*args, **kwargs):
        
        manager_form = ManagerField()
        return render(request,'manager/create.html',{'forms':manager_form})
@method_decorator(login_required,name='dispatch')
class ManagerList(View):
    
    def get(self,request,*args, **kwargs):
        
        manager_list = Manager.objects.all()
        mtx = {'managers':manager_list}
        return render(request,'manager/list.html',mtx)
@method_decorator(login_required,name='dispatch')
class ManagerDelete(View):
    
    def get(self,request,id,*args, **kwargs):
        
        manager = Manager.objects.get(id=id).delete()
        messages.success(request, 'Project Deleted!')
        return redirect('manager_list')
@method_decorator(login_required,name='dispatch')    
class UpdateManager(View):
    
    def get(self,request,id,*args, **kwargs):
        
        manager = get_object_or_404(Manager,id=id)
        manager_form = ManagerField(instance = manager)
        return render(request,'project/update.html',{'forms':manager_form})
    
    def post(self,request,id, *args, **kwargs):
        
        manager = get_object_or_404(Manager,id=id)
        manager_form = ManagerField(request.POST or None, instance = manager)
        if manager_form.is_valid():
            manager_form.save()
            messages.success(request, 'Successfully Employee Updated!')
            return redirect('manager_list')
        
