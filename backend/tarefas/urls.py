from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas),
    path('abertas/', views.listar_tarefas_abertas),
]