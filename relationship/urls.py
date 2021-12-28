from django .urls import path
from .import views

urlpatterns=[
    
    path('',views.home,name = 'home'),
    path('employee_list/',views.employee_list,name = 'employee_list'),
    path('create_employee/',views.create_employee,name = 'create_employee'),
    path('employee_delete/<int:id>/',views.employee_delete,name = 'employee_delete'),
    path('update_employee/<int:id>/',views.update_employee,name = 'update_employee'),
    path('create_project/',views.create_project,name = 'create_project'),
    path('project_delete/<int:id>/',views.project_delete,name = 'project_delete'),
    path('project_list',views.project_list,name = 'project_list'),
    path('update_project/<int:id>/',views.update_project,name = 'update_project'),
    path('create_manager/',views.create_manager,name = 'create_manager'),
    path('manager_list/',views.manager_list,name = 'manager_list'),
    path('delete_manager/<int:id>/',views.delete_manager,name = 'delete_manager'),
    path('update_manager/<int:id>/',views.update_manager,name = 'update_manager'),
]