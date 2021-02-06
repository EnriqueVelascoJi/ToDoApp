from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('inicio/', views.index),
    path('agregar_item/', views.agregar_item),
    path('eliminar_item/<int:id_borrar>', views.eliminar_item),
]