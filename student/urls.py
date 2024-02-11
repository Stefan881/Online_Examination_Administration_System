from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student, name='index-url'),
    path('administrator/', views.admin, name='admin-url'),
    path('instructor/', views.instructor, name='admin-url'),
    path('login/', views.login, name='login-url'),
]
