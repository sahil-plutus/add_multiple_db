from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('student', views.StudentAPI, basename="student_api")

urlpatterns = [
    path('', include(router.urls))
]
