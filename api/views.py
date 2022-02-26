from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, GroupSerializer, ClassroomSerializer
from .models import Student, Group


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/students',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of students'
        },
        {
            'Endpoint': '/classroom',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of classrooms'
        },
        {
            'Endpoint': '/group',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of groups'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_classroom(request):
    classrooms = Student.objects.all()
    serializer = ClassroomSerializer(classrooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_group(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)
