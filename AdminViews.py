import random
import uuid

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import *
from .models import *


def admin_home(request):
    return render(request, 'admin/admin_home.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('admin_home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'admin/change_password.html', {'form': form})


class RegisterStudentsView(View):
    form_class_u = StudentRegisterForm

    def get(self, request):
        form = self.form_class_u()
        return render(request, 'admin/add_student.html', {'form': form})

    def post(self, request):
        form = self.form_class_u(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            random_password = uuid.uuid4().hex
            user.set_password(random_password)
            username = (str(100) + str(random.randint(1000, 9000))).lower()
            while CustomUser.objects.filter(username=username).exists():
                username = username + str(random.randint(1, 9))
            user.username = username
            user.user_type = 3
            user.save()
            user.student.temp_password = random_password
            user.student.save()
            messages.success(request, f'Name: {user.first_name} {user.last_name} | Student ID: {user.username}'
                                      f' | Temp_password: {user.student.temp_password}'
                             )
            return redirect('view_student')

        return render(request, 'admin/add_student.html', {'form': form})


def student_view(request):
    student = CustomUser.objects.all().filter(user_type="3")
    return render(request, 'admin/view_student.html', {'student': student})


def student_delete(request, id):
    student = CustomUser.objects.get(pk=id)
    student.delete()
    return redirect('view_student')


def student_update(request, id):
    instance = get_object_or_404(Student, id=id)
    form = EditStudentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('view_student')
    return render(request, 'admin/edit_student.html', {'form': form, 'instance': instance})


def TeacherRegister(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 2
            user.save()
            return redirect('view_teacher')
    else:
        form = TeacherRegisterForm()
    return render(request, 'admin/add_teacher.html', {'form': form})


def teacher_view(request):
    teacher = CustomUser.objects.all().filter(user_type="2")
    return render(request, 'admin/view_teacher.html', {'teacher': teacher})


def teacher_delete(request, id):
    teacher = CustomUser.objects.get(pk=id)
    teacher.delete()
    return redirect('view_teacher')


def view_section(request):
    section = Section.objects.all()
    return render(request, 'admin/view_section.html', {'section': section})


def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_section')
    else:
        form = SectionForm()
    return render(request, 'admin/add_section.html', {'form': form})


def delete_section(request, id):
    section = Section.objects.get(pk=id)
    section.delete()
    return redirect('view_section')


def update_section(request, id):
    instance = get_object_or_404(Section, id=id)
    form = SectionForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('view_section')
    return render(request, 'admin/edit_section.html', {'form': form})


def view_subject(request):
    subject = Subject.objects.all()
    return render(request, 'admin/view_subject.html', {'subject': subject})


def update_subject(request, id):
    instance = get_object_or_404(Subject, id=id)
    form = SubjectForm(request.POST or None, instance=instance)
    if form.is_valid():
        if Subject.objects.filter(section_id=instance.section_id.id, time_id=instance.time_id).exists():
            messages.info(request, f'Time {instance.time_id} is already set to other subject in section'
                                    f' {instance.section_id}!')
            return redirect('update_subject', id=id)
        elif Subject.objects.filter(teacher_id=instance.teacher_id.id, time_id=instance.time_id).exists():
            messages.info(request, f'schedule for {instance.teacher_id}  already have this {instance.time_id}'
                                    f' time!')
            return redirect('update_subject', id=id)
        else:
            form.save()
        return redirect('view_subject')
    return render(request, 'admin/edit_subject.html', {'form': form, 'instance': instance})


def add_room(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_room')
    else:
        form = ClassroomForm()
    return render(request, 'admin/add_classroom.html', {'form': form})


def add_time(request):
    time = Time.objects.all()
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')
            messages.success(request, f'{start_time}-{end_time} Time has been added')
            return redirect('add_time')
    else:
        form = TimeForm()
    return render(request, 'admin/add_time.html', {'form': form, 'time': time})


def delete_time(request, id):
    time = Time.objects.get(pk=id)
    time.delete()
    return redirect('add_time')
