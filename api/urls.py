from django.urls import path
from . import views

urlpatterns = [

    path('', views.get_routes),
    path('places', views.get_place),
    path('academys', views.get_academys),
    path('academys/<str:pk>', views.get_academy),
    path('academys/<str:pk>/update', views.update_academy),
    path('academys/<str:pk>/delete', views.delete_academy),
    path('academys/create/', views.create_academy),
    path('students', views.get_student),
    path('teachers', views.get_teacher),
    path('classrooms', views.get_classroom),
    path('groups', views.get_group),
    path('presences', views.get_presence),

]