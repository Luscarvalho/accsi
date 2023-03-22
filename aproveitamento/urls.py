from django.urls import path
from aproveitamento import views

urlpatterns = [
    path('<int:pk>', views.ListarAproveitamento.as_view(), name="listar_aproveitamento"),
    path('cadastrar/<int:pk>', views.CadastrarAproveitamento.as_view(), name="cadastrar_aproveitamento"),
    path('editar/<int:pk>', views.EditarAproveitamento.as_view(), name="editar_aproveitamento"),
]
