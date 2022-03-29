from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student_Data
from .serializers import StudentSerializer


class StudentAPI(ModelViewSet):
    queryset = Student_Data.objects.all()
    serializer_class = StudentSerializer

