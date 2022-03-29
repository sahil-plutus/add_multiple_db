from django.shortcuts import render
from .models import Teacher_Data
from rest_framework.viewsets import ModelViewSet
from .serializers import TeacherSerializer


class TeacherAPI(ModelViewSet):
    queryset = Teacher_Data.objects.all()
    serializer_class = TeacherSerializer

    
