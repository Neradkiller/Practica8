from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from control import views

urlpatterns = [
    path('facultys/', views.faculty_list),
    path('facultys/<int:pk>', views.faculty_detail),
]