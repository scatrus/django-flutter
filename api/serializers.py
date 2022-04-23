from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from api.models import Teacher, Student, Academy, Place, Classroom, Group, Presence, CustomUser


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = CustomUser
        fields = (
            # 'username',
            # 'first_name',
            # 'last_name',
            'email',
            'password',
        )
        extra_kwargs = {'password': {'write_only': True}}
        validators = [
            UniqueTogetherValidator(
                queryset=CustomUser.objects.all(),
                fields=['email']

            )
        ]


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
