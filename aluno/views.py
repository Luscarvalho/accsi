from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Aluno


@method_decorator(login_required, name='dispatch')
class ListarAlunos(ListView):
    template_name = 'listar_aluno.html'
    model = Aluno
    context_object_name = 'alunos'


@method_decorator(login_required, name='dispatch')
class CadastrarAluno(CreateView):
    template_name = 'cadastrar_aluno.html'
    model = Aluno
    fields = ['nome', 'matricula', 'email', 'telefone']
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class EditarAluno(UpdateView):
    template_name = 'cadastrar_aluno.html'
    model = Aluno
    fields = ['nome', 'matricula', 'email', 'telefone']
    success_url = reverse_lazy('home')
