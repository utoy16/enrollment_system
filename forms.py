from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Section, Student, Enrolled, Classroom, Time, Subject


class TeacherRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.fields['adviser_id'].queryset = CustomUser.objects.filter(user_type='2')


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['grade_level']


class EnrolledForm(forms.ModelForm):
    class Meta:
        model = Enrolled
        fields = ['subject_id']

    def __init__(self, *args, **kwargs):
        id = kwargs.pop('id')
        super(EnrolledForm, self).__init__(*args, **kwargs)
        self.fields['subject_id'].queryset = Subject.objects.filter(section_id=id)


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['teacher_id', 'time_id', 'room_id']

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields['teacher_id'].queryset = CustomUser.objects.filter(user_type='2')


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'


class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = '__all__'

