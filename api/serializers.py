from rest_framework.serializers import ModelSerializer
from .models import Student, Group, Classroom


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ClassroomSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
