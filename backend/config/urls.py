from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/tarefas/', include('tarefas.urls')),
    path('api/usuarios/', include('usuarios.urls')),
]