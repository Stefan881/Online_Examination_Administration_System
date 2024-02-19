from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student, name='index-url'),
    path('administrator/', views.admin, name='admin-url'),
    path('instructor/', views.instructor, name='admin-url'),
    path('marks/', views.marks, name='marks-url'),
    path('available_examination/', views.available_examinations, name='available_examination_url'),
    path('student_click/', views.student_click, name='student_click_url'),
    path('login/', views.login, name='login-url'),
    path('register/', views.register, name='register-url'),
]
