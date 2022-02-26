from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('places', views.get_place),
    path('academys', views.get_academy),
    path('students', views.get_student),
    path('teachers', views.get_teacher),
    path('classrooms', views.get_classroom),
    path('groups', views.get_group),
    path('presences', views.get_presence),

]
