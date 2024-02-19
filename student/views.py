from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def student(request):
    return render(request, 'student.html', {})


def admin(request):
    return render(request, 'administrator.html', {})


def instructor(request):
    return render(request, 'instructor.html', {})


def marks(request):
    return render(request, 'student/Marks.html', {})


def available_examinations(request):
    return render(request, 'student/Available Examination.html', {})


def register(request):
    return render(request, 'register.html', {})


def student_click(request):
    return render(request,'student/student_click.html',{})

def login(request):
    if request.method == 'POST':
        username = request.method['username']
        password = request.method['password']
        user = authenticate(request, username=username, password=password)
        login(user)
        return redirect('admin-url')
    else:
        return render(request, 'login.html', {})

    # return render(request, 'login.html', {})
