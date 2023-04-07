from django.urls import path
from . import views
from .forms import StudentRegForm, CounsellorRegForm, AgencyRegForm

urlpatterns = [
    path('register/student/', views.StudentRegisterView.as_view(), name='register_student'),
    path('register/counsellor/', views.CounsellorRegisterView.as_view(), name='register_counsellor'),
    path('register/agent/', views.AgentRegisterView.as_view(), name='register_agent'),

    path('update/student/',
        views.AbstractUpdateView.as_view(form_class = StudentRegForm),
        name='update_student'),

    path('update/counsellor/',
        views.AbstractUpdateView.as_view(form_class = CounsellorRegForm),
        name='update_counsellor'),

    path('update/agent/',
        views.AbstractUpdateView.as_view(form_class = AgencyRegForm),
        name='update_agent'),

    path('update/password/', views.change_password, name='change_password'),

    path('home/student/', views.student_home_view, name='student_home'),
    path('home/counsellor/', views.counsellor_home_view, name='counsellor_home'),
    path('home/agency/', views.agency_home_view, name='agency_home'),
    
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout')
]
