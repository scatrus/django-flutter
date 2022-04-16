from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Teacher, Student, Academy, Place, Classroom, Group, Presence
from api.serializers import TeacherSerializer, StudentSerializer, AcademySerializer, PlaceSerializer, \
    ClassroomSerializer, GroupSerializer, PresenceSerializer


@api_view(['GET', 'POST'])
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
def teacher_detail(request, pk):
    try:
        item = Teacher.objects.get(pk=pk)
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
def student_detail(request, pk):
    try:
        item = Student.objects.get(pk=pk)
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
