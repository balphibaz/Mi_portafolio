from django.urls import path
from .views import TecnologiasView, ProyectosView  # Asegúrate de importar tus vistas

urlpatterns = [
    path('tecnologias/', TecnologiasView.as_view(), name='tecnologias'),
    path('proyectos/', ProyectosView.as_view(), name='proyectos'),
]