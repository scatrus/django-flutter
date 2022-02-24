from django.contrib.contenttypes.models import ContentType
from django.db import models


class User(models.Model):
    class Meta:
        abstract = True

    code = models.PositiveSmallIntegerField(default=None)
    name = models.CharField(max_length=255, default=None)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Teacher(User):
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(User):
    presence_amount = models.PositiveSmallIntegerField(default=None)
    level = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Academy(models.Model):
    name = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name


class Place(models.Model):
    place_name = models.CharField(max_length=100, default=None)
    tatame_amount = models.PositiveSmallIntegerField(default=None)
    id_academy = models.ForeignKey(Academy, on_delete=models.CASCADE, related_name='place_academy',
                                   verbose_name='Sala/Local/Espaço', default=None)

    def __str__(self):
        return self.place_name


class Classroom(models.Model):
    date = models.DateTimeField()
    id_place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='classroom_place',
                                 verbose_name='Sala/Local/Espaço')
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classroom_teacher',
                                   verbose_name='Professor')

    def __str__(self):
        return str(self.date)


class Group(models.Model):
    id_student = models.ManyToManyField(Student, related_name='group_student')
    id_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='group_classroom',
                                     verbose_name='Turma/Grupo/Alunos')

    def __str__(self):
        return 'Grupo X'


class Presence(models.Model):
    ...
# tabela pivô - criar campo de presença com vários tipos: presente, falta, falta justificada, etc.
# ver documentação
