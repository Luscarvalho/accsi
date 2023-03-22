from django.urls import path, include

urlpatterns = [
    path('', include('aluno.urls')),
    path('login/', include('user.urls')),
    path('modalidade/', include('modalidade.urls')),
    path('atividade/', include('atividade.urls')),
    path('aproveitamento/', include('aproveitamento.urls')),
]
