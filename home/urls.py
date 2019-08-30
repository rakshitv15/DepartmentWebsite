from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('login/', views.user_login, name='login'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('announcements/', views.announcements, name='announcements'),
    path('course_ms/', views.course_ms, name='course_ms'),
    path('course_mtech/', views.course_mtech, name='course_mtech'),
    path('course_phd/', views.course_phd, name='course_phd'),
    path('facilities/', views.facilities, name='facilities'),
    path('faculty/', views.faculty, name='faculty'),
    path('project_dyslexia/', views.project_dyslexia, name='project_dyslexia'),
    path('project_ide/', views.project_ide, name='project_ide'),
    path('project_nptel/', views.project_nptel, name='project_nptel'),
    path('project_pedagogy/', views.project_pedagogy, name='project_pedagogy'),
    path('projects/', views.projects, name='projects'),
    path('research_areas/', views.research_areas, name='research_areas'),
    path('staff/', views.staff, name='staff'),
    path('students/', views.students, name='students'),
]