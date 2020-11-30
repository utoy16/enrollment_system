from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subject, Section, Enrolled, Student


def student_home(request):
    return render(request, 'student/student_home.html')


def student_enroll(request):
    selected_section = None
    section = Section.objects.filter(grade_level=request.user.student.grade_level)
    subject = Subject.objects.all()
    if request.method == 'POST':
        selected_section = request.POST['section']
        subject = Subject.objects.filter(section_id=selected_section)

    context = {
        'section': section,
        'subject': subject,
        'selected_section': selected_section,
    }
    return render(request, 'student/student_enroll.html', context)


def student_enroll_save(request, id):
    section = Section.objects.filter(pk=id)
    enroll = Enrolled.objects.all()
    subject = Subject.objects.filter(section_id=id)
    if request.method == 'POST':
        if request.user.student.enrolled == 0:
            for subject in subject:
                enrolled = Enrolled.objects.create(subject_id=subject)
                enrolled.save()

            user_enroll = Student.objects.get(admin=request.user)
            user_enroll.enrolled = 1
            user_enroll.save()
            return redirect('student_schedule')
        else:
            messages.info(request, f'Student is already enrolled')

    context = {
        'subject': subject,
        'enroll': enroll,
        'section': section,
    }
    return render(request, 'student/student_enroll_save.html', context)


def student_schedule(request):
    enroll = Enrolled.objects.filter(student_id=request.user)
    return render(request, 'student/student_schedule.html', {'enroll': enroll})
