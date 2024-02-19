from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from . import forms,models
from django.contrib.auth.decorators import login_required


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
    return render(request, 'student/student_click.html', {})


def landing(request):
    return render(request, 'landing_page.html', {})


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


def student_signup_view(request):
    userForm = forms.StudentUserForm()
    studentForm = forms.StudentForm()
    mydict = {'userForm': userForm, 'studentForm': studentForm}
    if request.method == 'POST':
        userForm = forms.StudentUserForm(request.POST)
        studentForm = forms.StudentForm(request.POST, request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            student = studentForm.save(commit=False)
            student.user = user
            student.save()
            # my_student_group = Group.objects.get_or_create(name='STUDENT')
            # my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request, 'register.html', context=mydict)
