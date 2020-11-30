from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_userforeignkey.models.fields import UserForeignKey

GENDER_CHOICES = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
)
LEVEL_CHOICES = (
    ('Grade 1', 'Grade 1'), ('Grade 2', 'Grade 2'), ('Grade 3', 'Grade 3'),
    ('Grade 4', 'Grade 4'), ('Grade 5', 'Grade 5'), ('Grade 6', 'Grade 6'),
)


class SchoolYear(models.Model):
    id = models.AutoField(primary_key=True)
    school_start_year = models.DateField()
    school_end_year = models.DateField()
    objects = models.Manager()


class SubjectGrade1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Subject Name', max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class SubjectGrade2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Subject Name', max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class SubjectGrade3(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Subject Name', max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class SubjectGrade4(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Subject Name', max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class SubjectGrade5(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Subject Name', max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class SubjectGrade6(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Subject Name', max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Teacher"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    enrolled = models.IntegerField(default=0)
    grade_level = models.CharField(choices=LEVEL_CHOICES, max_length=10, default='Grade 1')
    temp_password = models.CharField(max_length=10)
    address = models.CharField(max_length=500, null=True, blank=True)
    birthday = models.DateField(verbose_name="Birthday", null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    guardian_name = models.CharField("Parents/Guardian Name", max_length=255, null=True, blank=True)
    guardian_address = models.CharField(max_length=500, null=True, blank=True)
    contact_no = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=255)
    grade_level = models.CharField(choices=LEVEL_CHOICES, max_length=10)
    adviser_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.section_name}'


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.room_name}'


class Time(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


SUBJECT_CHOICES = (
    ('Filipino', 'Filipino'),
    ('English', 'English'),
    ('Mathematics', 'Mathematics'),
    ('Science', 'Science'),
    ('Araling Panlipunan', 'Araling Panlipunan'),
    ('Edukasyon sa Pagpapakatao', 'Edukasyon sa Pagpapakatao'),
    ('Edukasyong Pantahanan at Pangkabuhayan', 'Edukasyong Pantahanan at Pangkabuhayan'),
    ('MAPEH', 'MAPEH'),
    ('Mother Tongue', 'Mother Tongue'),
)


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject_name = models.CharField(choices=SUBJECT_CHOICES, max_length=255)
    teacher_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Teacher', null=True, blank=True)
    subject_level = models.CharField(max_length=20, default='Grade 1')
    time_id = models.ForeignKey(Time, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Time')
    room_id = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Room')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.section_id} - {self.subject_level} - {self.subject_name} - {self.teacher_id} - {self.time_id} - {self.room_id} '


class Enrolled(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = UserForeignKey(auto_user_add=True, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Teacher.objects.create(admin=instance)
        if instance.user_type == 3:
            Student.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.teacher.save()
    if instance.user_type == 3:
        instance.student.save()


@receiver(post_save, sender=Section)
def create_subject(sender, instance, created, **kwargs):
    if created:
        if instance.grade_level == "Grade 1":
            Subject.objects.create(section_id=instance, subject_name="Filipino", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Mathematics", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Araling Panlipunan",
                                   subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Edukasyon sa Pagpapakatao",
                                   subject_level=instance.grade_level)
            subject = Subject.objects.create(section_id=instance, subject_name="Mother Tongue",
                                             subject_level=instance.grade_level)
            subject.save()
        if instance.grade_level == "Grade 2":
            Subject.objects.create(section_id=instance, subject_name="Filipino", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Mathematics", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Araling Panlipunan",
                                   subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Edukasyon sa Pagpapakatao",
                                   subject_level=instance.grade_level)
            subject = Subject.objects.create(section_id=instance, subject_name="Mother Tongue",
                                             subject_level=instance.grade_level)
            subject.save()
        if instance.grade_level == "Grade 3":
            Subject.objects.create(section_id=instance, subject_name="Filipino", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Mathematics", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Araling Panlipunan",
                                   subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Edukasyon sa Pagpapakatao",
                                   subject_level=instance.grade_level)
            subject = Subject.objects.create(section_id=instance, subject_name="Mother Tongue",
                                             subject_level=instance.grade_level)
            subject.save()
        if instance.grade_level == "Grade 4":
            Subject.objects.create(section_id=instance, subject_name="Filipino", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="English", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Mathematics", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Science", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Araling Panlipunan",
                                   subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Edukasyong Pantahanan at Pangkabuhayan",
                                   subject_level=instance.grade_level)
            subject = Subject.objects.create(section_id=instance, subject_name="MAPEH",
                                             subject_level=instance.grade_level)
            subject.save()
        if instance.grade_level == "Grade 5":
            Subject.objects.create(section_id=instance, subject_name="Filipino", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="English", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Mathematics", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Science", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Araling Panlipunan",
                                   subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Edukasyong Pantahanan at Pangkabuhayan",
                                   subject_level=instance.grade_level)
            subject = Subject.objects.create(section_id=instance, subject_name="MAPEH",
                                             subject_level=instance.grade_level)
            subject.save()
        if instance.grade_level == "Grade 6":
            Subject.objects.create(section_id=instance, subject_name="Filipino", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="English", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Mathematics", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Science", subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Araling Panlipunan",
                                   subject_level=instance.grade_level)
            Subject.objects.create(section_id=instance, subject_name="Edukasyong Pantahanan at Pangkabuhayan",
                                   subject_level=instance.grade_level)
            subject = Subject.objects.create(section_id=instance, subject_name="MAPEH",
                                             subject_level=instance.grade_level)
            subject.save()
