from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from control import views

urlpatterns = [
    path('facultys/', views.faculty_list),
    path('facultys/<int:pk>', views.faculty_detail),
    path('persons/', views.person_list),
    path('persons/<int:pk>', views.person_detail),
    path('schools/', views.school_list),
    path('schools/<int:pk>', views.school_detail),
    path('sections/', views.section_list),
    path('sections/<int:pk>', views.section_detail),
    path('sections/<int:pk>/students', views.section_students),
    path('sections/<int:pk>/teacher', views.section_teacher),
    path('enrollments/', views.enrollment_list),
    path('enrollments/<int:pk>/', views.enrollment_detail),
]