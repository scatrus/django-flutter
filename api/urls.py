from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('students', views.get_student),
    path('classrooms', views.get_classroom),
    path('groups', views.get_group),

]
