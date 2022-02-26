from rest_framework.serializers import ModelSerializer
from .models import Student, Group, Classroom, Teacher, Academy, Place, Presence


class AcademySerializer(ModelSerializer):
    class Meta:
        model = Academy
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ClassroomSerializer(ModelSerializer):
    model = Classroom
    fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PresenceSerializer(ModelSerializer):
    class Meta:
        model = Presence
        fields = '__all__'

