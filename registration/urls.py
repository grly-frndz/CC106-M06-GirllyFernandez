
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_registration, name='student_registration'),
    path('success/<str:first_name>/', views.registration_success, name='registration_success'),
]
