from rest_framework import viewsets

from app_student.models import Students
from app_student.view.serializers.sz_students import StudentsSerializer, UpdateStudentSerializer, \
    CreateStudentSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    lookup_fields = ['name', 'age']

    def get_serializer_class(self):
        methodes_list = dict(PUT=UpdateStudentSerializer,   POST=CreateStudentSerializer)
        return methodes_list.get(self.request.method, StudentsSerializer)
