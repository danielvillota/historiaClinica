from django.urls import path
from .views import PacientesApiView


urlpatterns = [
    path('usuarios', PacientesApiView.as_view(),name="listar_pacientes"),
]
