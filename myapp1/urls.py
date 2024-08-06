from django.contrib import admin
from django.urls import path
from . import views  # Importa las vistas desde tu archivo views.py

urlpatterns = [
    path('', views.inicio, name='Inicio'),  # Ruta para la página de inicio
    path('experiencias/', views.experiencia_list, name='experiencia_list'),
    path('experiencias/<int:pk>/', views.experiencia_detail, name='experiencia_detail'),
    path('experiencias/create/', views.experiencia_create, name='experiencia_create'),
    path('experiencias/<int:pk>/update/', views.experiencia_update, name='experiencia_update'),
    path('experiencias/<int:pk>/delete/', views.experiencia_delete, name='experiencia_delete'),
    path('aprendices/', views.aprendiz_list, name='aprendiz_list'),
    path('aprendices/<int:pk>/', views.aprendiz_detail, name='aprendiz_detail'),
    path('aprendices/create/', views.aprendiz_create, name='aprendiz_create'),
    path('aprendices/<int:pk>/update/', views.aprendiz_update, name='aprendiz_update'),
    path('aprendices/<int:pk>/delete/', views.aprendiz_delete, name='aprendiz_delete'),
    path('mentores/', views.mentor_list, name='mentor_list'),
    path('mentores/<int:pk>/', views.mentor_detail, name='mentor_detail'),
    path('mentores/create/', views.mentor_create, name='mentor_create'),
    path('mentores/<int:pk>/update/', views.mentor_update, name='mentor_update'),
    path('mentores/<int:pk>/delete/', views.mentor_delete, name='mentor_delete'),
    path('actividades/', views.actividad_list, name='actividad_list'),
    path('actividades/<int:pk>/', views.actividad_detail, name='actividad_detail'),
    path('actividades/create/', views.actividad_create, name='actividad_create'),
    path('actividades/<int:pk>/update/', views.actividad_update, name='actividad_update'),
    path('actividades/<int:pk>/delete/', views.actividad_delete, name='actividad_delete'),
    path('niveles/', views.nivel_list, name='nivel_list'),
    path('niveles/<int:pk>/', views.nivel_detail, name='nivel_detail'),
    path('niveles/create/', views.nivel_create, name='nivel_create'),
    path('niveles/<int:pk>/update/', views.nivel_update, name='nivel_update'),
    path('niveles/<int:pk>/delete/', views.nivel_delete, name='nivel_delete'),
]
