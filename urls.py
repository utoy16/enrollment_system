from django.conf.urls import url
from django.urls import path
from . import views
from . import AdminViews, StudentViews, TeacherViews
from .AdminViews import RegisterStudentsView

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    # Admin URL
    path('admin_home/', AdminViews.admin_home, name='admin_home'),
    url(r'^admin/password/$', AdminViews.change_password, name='change_password_admin'),
    path('add_student', RegisterStudentsView.as_view(), name='add_student'),
    path('view_student', AdminViews.student_view, name='view_student'),
    path('update_student/<int:id>', AdminViews.student_update, name='edit_student'),
    path('delete_student/<int:id>', AdminViews.student_delete),
    path('add_teacher', AdminViews.TeacherRegister, name='add_teacher'),
    path('view_teacher', AdminViews.teacher_view, name='view_teacher'),
    path('delete_teacher/<int:id>', AdminViews.teacher_delete),
    path('add_section/', AdminViews.add_section, name='add_section'),
    path('view_section/', AdminViews.view_section, name='view_section'),
    path('update_section/<int:id>', AdminViews.update_section, name='edit_section'),
    path('delete_section/<int:id>', AdminViews.delete_section),
    path('view_subject/', AdminViews.view_subject, name='view_subject'),
    path('update_subject/<int:id>', AdminViews.update_subject, name='update_subject'),
    path('add_room/', AdminViews.add_room, name='add_room'),
    path('add_time/', AdminViews.add_time, name='add_time'),
    path('delete_time/<int:id>', AdminViews.delete_time),
    # Teacher URL
    path('teacher_home/', TeacherViews.teacher_home, name='teacher_home'),
    path('teacher_schedule/', TeacherViews.teacher_schedule, name='teacher_schedule'),
    path('teacher_student_list/<int:id>', TeacherViews.teacher_student_list, name='teacher_student_list'),
    url(r'^teacher/password/$', TeacherViews.change_password, name='change_password'),
    # Student URL
    path('student_home/', StudentViews.student_home, name='student_home'),
    path('student_temp_change_password', views.temp_change_password, name='temp_change_password'),
    path('student_enroll/', StudentViews.student_enroll, name='student_enroll'),
    path('student_enroll_save/<int:id>', StudentViews.student_enroll_save, name='student_enroll_save'),
    path('student_schedule', StudentViews.student_schedule, name='student_schedule')
]
