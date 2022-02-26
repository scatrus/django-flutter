from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, GroupSerializer, ClassroomSerializer, TeacherSerializer, AcademySerializer, \
    PlaceSerializer, PresenceSerializer
from .models import Student, Group, Classroom, Teacher, Academy, Place, Presence


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/places',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of places'
        },
        {
            'Endpoint': '/academys',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of academys'
        },
        {
            'Endpoint': '/students',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of students'
        },
        {
            'Endpoint': '/teachers',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of teachers'
        },
        {
            'Endpoint': '/classrooms',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of classrooms'
        },

        {
            'Endpoint': '/presences',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of presences'
        },
        {
            'Endpoint': '/groups',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of groups'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def get_presence(request):
    presences = Presence.objects.all()
    serializer = PresenceSerializer(presences, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_place(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_academy(request):
    academys = Academy.objects.all()
    serializer = AcademySerializer(academys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_teacher(request):
    students = Teacher.objects.all()
    serializer = TeacherSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_classroom(request):
    classrooms = Classroom.objects.all()
    serializer = ClassroomSerializer(classrooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_group(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)
