from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .models import Subject, Section, Enrolled


def teacher_home(request):
    return render(request, 'teacher/teacher_home.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('teacher_home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'teacher/change_password.html', {'form': form})


def teacher_schedule(request):
    try:
        section = Section.objects.get(adviser_id=request.user.id)
    except Section.DoesNotExist:
        section = None

    subject = Subject.objects.filter(teacher_id=request.user.id)
    return render(request, 'teacher/teacher_subject.html', {'subject': subject, 'section': section})


def teacher_student_list(request, id):
    student_list = Enrolled.objects.filter(subject_id=id).order_by('student_id__last_name')
    subject = Subject.objects.get(id=id)
    context = {
        'student_list': student_list,
        'subject': subject,
    }
    return render(request, 'teacher/teacher_student_list.html', context)
