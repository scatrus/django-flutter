from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User as BaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from api.managers import CustomUserManager

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Teacher(CustomUser):
    level = models.CharField(max_length=100)

    class Meta:
        verbose_name: 'Teacher'


class Student(CustomUser):
    presence_amount = models.PositiveSmallIntegerField(default=0)
    level = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name: 'Student'


class Academy(models.Model):
    name = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name


class Place(models.Model):
    place_name = models.CharField(max_length=100, default=None)
    tatame_amount = models.PositiveSmallIntegerField(default=None)
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE, related_name='place_academy',
                                verbose_name='Academia', default=None)

    def __str__(self):
        return self.place_name


class Classroom(models.Model):
    date = models.DateTimeField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='classroom_place',
                              verbose_name='Sala/Local/Espaço')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classroom_teacher',
                                verbose_name='Professor')

    def __str__(self):
        return str(self.date)


class Group(models.Model):
    members = models.ManyToManyField(Student, related_name='group_student')
    # through='Presence',
    # through_fields=('group', 'student'), )
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='group_classroom',
                                  verbose_name='Turma/Grupo/Alunos')

    def __str__(self):
        return str(self.members.all().values_list('name'))


class Presence(models.Model):
    PRESENCE_CHOICES = (
        (1, 'PRESENCE'),
        (0, 'ABSENCE'),
        (2, 'EXCUSED ABSENCE'),
        (3, 'UNEXCUSED ABSENCE'),
    )

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    presence = models.PositiveSmallIntegerField(choices=PRESENCE_CHOICES)

    def __str__(self):
        return f'{self.student.name} - {self.get_presence_display()} - {self.group.classroom.date}'


@receiver(post_save, sender=Presence)
def update_presence(sender, instance, **kwargs):
    if instance.presence == 1:  # sum only if presence code is 1
        instance.student.presence_amount += instance.presence
        instance.student.save()
