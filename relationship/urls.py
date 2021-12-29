from django .urls import path
from .import views

urlpatterns=[
    
    path('',views.Home.as_view(),name = 'home'),
    path('employee_list/',views.EmployeeList.as_view(),name = 'employee_list'),
    path('create_employee/',views.CreateEmployee.as_view(),name = 'create_employee'),
    path('employee_delete/<int:pk>/',views.EmployeeDelete.as_view(),name = 'employee_delete'),
    path('update_employee/<int:pk>/',views.UpdataEmployee.as_view(),name = 'update_employee'),
    path('create_project/',views.CreateProject.as_view(),name = 'create_project'),
    path('project_delete/<int:pk>/',views.ProjectDelete.as_view(),name = 'project_delete'),
    path('project_list',views.ProjectList.as_view(),name = 'project_list'),
    path('update_project/<int:pk>/',views.UpdateProject.as_view(),name = 'update_project'),
    path('create_manager/',views.CreateManager.as_view(),name = 'create_manager'),
    path('manager_list/',views.ManagerList.as_view(),name = 'manager_list'),
    path('delete_manager/<int:pk>/',views.ManagerDelete.as_view(),name = 'delete_manager'),
    path('update_manager/<int:pk>/',views.UpdateManager.as_view(),name = 'update_manager'),
    
]