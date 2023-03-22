from django.urls import path
from atividade import views

urlpatterns = [
    path('ensino', views.ListarEnsino.as_view(), name="listar_atividade_ensino"),
    path('ensino/cadastrar', views.CadastrarEnsino.as_view(), name="cadastrar_atividade_ensino"),
    path('ensino/editar/<int:pk>', views.EditarEnsino.as_view(), name="editar_atividade_ensino"),
    path('pesquisa', views.ListarPesquisa.as_view(), name="listar_atividade_pesquisa"),
    path('pesquisa/cadastrar', views.CadastrarPesquisa.as_view(), name="cadastrar_atividade_pesquisa"),
    path('pesquisa/editar/<int:pk>', views.EditarPesquisa.as_view(), name="editar_atividade_pesquisa"),
    path('extensao', views.ListarExtensao.as_view(), name="listar_atividade_extensao"),
    path('extensao/cadastrar', views.CadastrarExtensao.as_view(), name="cadastrar_atividade_extensao"),
    path('extensao/editar/<int:pk>', views.EditarExtensao.as_view(), name="editar_atividade_extensao"),
]
