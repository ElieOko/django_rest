from rest_framework import serializers

from app_student.models import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ["is_active",  "status"]


class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name',   'age',    'genre',   'promotion']
