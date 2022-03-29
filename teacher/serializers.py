from rest_framework import serializers
from .models import Teacher_Data


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_Data
        fields = '__all__'