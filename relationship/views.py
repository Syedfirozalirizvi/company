from django.shortcuts import get_object_or_404, render,redirect
from .forms import EmployeeForm , ProjectForm , ManagerField
from .models import Employee , Project , Manager
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request, 'Successfully Employee Created!')
            return redirect('employee_list')
            
    employee_form = EmployeeForm()
    return render(request,'employee/create.html',{'forms':employee_form})

def employee_list(request):
    employee_list = Employee.objects.all()
    ctx = {'employees':employee_list}
    return render(request,'employee/list.html',ctx)

def employee_delete(request,id):
    employee = Employee.objects.get(id=id).delete()
    messages.success(request, 'Employee Deleted!')
    return redirect('employee_list')
    
def update_employee(request,id):
    employee = get_object_or_404(Employee, id = id)
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST or None, instance = employee)
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request, 'Successfully Employee Updated!')
            return redirect('employee_list')
    employee_form = EmployeeForm(instance = employee)
    return render(request,'employee/update.html',{'forms':employee_form})


def create_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
        return redirect('project_list')
    project_form = ProjectForm()
    return render(request,'project/create.html',{'forms':project_form})


def project_list(request):
    project_list = Project.objects.all()
    ptx = {'projects':project_list}
    return render(request,'project/list.html',ptx)

def project_delete(request,id):
    project = Project.objects.get(id=id).delete()
    messages.success(request, 'Project Deleted!')
    return redirect('project_list')

def update_project(request,id):
    project = get_object_or_404(Project,id=id)
    if request.method == 'POST':
        project_form = ProjectForm(request.POST or None, instance = project)
        if project_form.is_valid():
            project_form.save()
            messages.success(request, 'Successfully Employee Updated!')
            return redirect('project_list')
    project_form = ProjectForm(instance = project)
    return render(request,'project/update.html',{'forms':project_form})
        
    

def create_manager(request):
    if request.method == 'POST':
        manager_form = ManagerField(request.POST)
        if manager_form.is_valid():
            manager_form.save()
        return redirect('manager_list')
    manager_form = ManagerField()
    return render(request,'manager/create.html',{'forms':manager_form})

def manager_list(request):
    manager_list = Manager.objects.all()
    mtx = {'managers':manager_list}
    return render(request,'manager/list.html',mtx)

def delete_manager(request,id):
    manager = Manager.objects.get(id=id).delete()
    messages.success(request, 'Project Deleted!')
    return redirect('manager_list')
    
def update_manager(request,id):
    manager = get_object_or_404(Manager,id=id)
    if request.method == 'POST':
        manager_form = ManagerField(request.POST or None, instance = manager)
        if manager_form.is_valid():
            manager_form.save()
            messages.success(request, 'Successfully Employee Updated!')
            return redirect('manager_list')
    manager_form = ManagerField(instance = manager)
    return render(request,'project/update.html',{'forms':manager_form})
        
