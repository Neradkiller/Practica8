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
]