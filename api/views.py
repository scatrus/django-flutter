from rest_framework import status, views, generics, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Teacher, Student, Academy, Place, Classroom, Group, Presence, CustomUser
from api.serializers import TeacherSerializer, StudentSerializer, AcademySerializer, PlaceSerializer, \
    ClassroomSerializer, GroupSerializer, PresenceSerializer, UserSerializer


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def teacher_list(request):
    if request.method == 'GET':
        items = Teacher.objects.order_by('pk')
        serializer = TeacherSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def teacher_detail(request, pk):
    try:
        item = get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = TeacherSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def student_list(request):
    if request.method == 'GET':
        items = Student.objects.order_by('pk')
        serializer = StudentSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def student_detail(request, pk):
    try:
        item = get()
    except Student.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def academy_list(request):
    if request.method == 'GET':
        items = Academy.objects.order_by('pk')
        serializer = AcademySerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AcademySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def academy_detail(request, pk):
    try:
        item = Academy.objects.get(pk=pk)
    except Academy.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AcademySerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AcademySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def place_list(request):
    if request.method == 'GET':
        items = Place.objects.order_by('pk')
        serializer = PlaceSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def place_detail(request, pk):
    try:
        item = Place.objects.get(pk=pk)
    except Place.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PlaceSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlaceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def classroom_list(request):
    if request.method == 'GET':
        items = Classroom.objects.order_by('pk')
        serializer = ClassroomSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def classroom_detail(request, pk):
    try:
        item = Classroom.objects.get(pk=pk)
    except Classroom.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ClassroomSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClassroomSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def group_list(request):
    if request.method == 'GET':
        items = Group.objects.order_by('pk')
        serializer = GroupSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def group_detail(request, pk):
    try:
        item = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = GroupSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def presence_list(request):
    if request.method == 'GET':
        items = Presence.objects.order_by('pk')
        serializer = PresenceSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PresenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def presence_detail(request, pk):
    try:
        item = Presence.objects.get(pk=pk)
    except Presence.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PresenceSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PresenceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


from rest_framework.generics import CreateAPIView


class UserCreateApiView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get(self, format=None):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class UserRecordView(generics.CreateAPIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [AllowAny]

    def get(self, format=None):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


def get(request, format=None):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'head']

    def post(self, request, format=None):
        self.http_method_names.append("GET")

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
