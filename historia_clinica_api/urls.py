from django.urls import path
from .views import HistoriasApiView, PacientesApiView


urlpatterns = [
    path('historias', HistoriasApiView.as_view(), name="listar_historias"),
    path('historias/<int:id>', HistoriasApiView.as_view() ,name="procesar_historias"),
    path('users', PacientesApiView.as_view(), name="listar_usuarios"),
]