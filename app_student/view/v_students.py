from rest_framework import viewsets

from app_student.models import Students
from app_student.view.serializers.sz_students import StudentsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
