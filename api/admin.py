from django.contrib import admin

from .models import Student, Teacher, Academy, Place, Classroom, Group, Presence

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Academy)
admin.site.register(Place)
admin.site.register(Classroom)
admin.site.register(Group)
admin.site.register(Presence)


