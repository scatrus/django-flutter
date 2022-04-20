from rest_framework.serializers import ModelSerializer
from api.models import Teacher, Student, Academy, Place, Classroom, Group, Presence


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        depth = 2
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        depth = 2
        fields = '__all__'


class AcademySerializer(ModelSerializer):
    class Meta:
        model = Academy
        depth = 2
        fields = '__all__'


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        depth = 2
        fields = '__all__'


class ClassroomSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        depth = 2
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        depth = 2
        fields = '__all__'


class PresenceSerializer(ModelSerializer):
    class Meta:
        model = Presence
        depth = 2
        fields = '__all__'
