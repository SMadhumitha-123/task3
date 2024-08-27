from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),  # Display all employees
    path('add/', views.add_employee, name='add_employee'),  # Add new employee (admin only)
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),  # Delete employee (admin only)
    path('signup/', views.sign_up, name='signup'),  # User sign-up
    path('',views.home,name='home'),
]
