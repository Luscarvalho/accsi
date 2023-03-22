from django.urls import path
from modalidade import views

urlpatterns = [
    path('', views.ListarModalidade.as_view(), name="listar_modalidade"),
]
