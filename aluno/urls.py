from django.urls import path
from aluno import views

urlpatterns = [
    path('', views.ListarAlunos.as_view(), name="home"),
    path('cadastrar/', views.CadastrarAluno.as_view(), name="cadastrar_aluno"),
    path('editar/<int:pk>', views.EditarAluno.as_view(), name="editar_aluno"),
]
