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
            'Endpoint': '/academys/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single academy object'
        },
        {
            'Endpoint': '/academys/create/',
            'method': 'POST',
            'body': {'name': ""},
            'description': 'Creates a new academy'
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
def get_academys(request):
    academys = Academy.objects.all()
    serializer = AcademySerializer(academys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_academy(request, pk):
    academy = Academy.objects.get(id=pk)
    serializer = AcademySerializer(academy, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_academy(request):
    data = request.data
    academy = Academy.objects.create(
        name=data['name']
    )
    serializer = AcademySerializer(academy, many=False)
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
