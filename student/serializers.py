from rest_framework import serializers
from .models import Student_Data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Data
        fields = '__all__'

