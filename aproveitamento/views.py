from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Aproveitamento, Aluno
import pandas as pd
from django.http import HttpResponse


@method_decorator(login_required, name='dispatch')
class ListarAproveitamento(ListView):
    template_name = 'listar_aproveitamento.html'
    model = Aproveitamento
    context_object_name = 'aproveitamentos'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_aluno = None

    def dispatch(self, request, *args, **kwargs):
        self.id_aluno = kwargs.get('pk', None)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(aluno=Aluno.objects.get(id_aluno=self.id_aluno))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_aluno'] = self.id_aluno
        return context


@method_decorator(login_required, name='dispatch')
class CadastrarAproveitamento(CreateView):
    template_name = 'cadastrar_aproveitamento.html'
    model = Aproveitamento
    fields = ['descricao', 'categoria', 'semestre', 'ano', 'ch']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_aluno = None

    def get_success_url(self):
        id_aluno = self.kwargs['pk']
        return reverse_lazy('listar_aproveitamento', kwargs={'pk': id_aluno})

    def dispatch(self, request, *args, **kwargs):
        self.id_aluno = kwargs.get('pk', None)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.aluno = Aluno.objects.get(id_aluno=self.id_aluno)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditarAproveitamento(UpdateView):
    template_name = 'cadastrar_aproveitamento.html'
    model = Aproveitamento
    fields = ['descricao', 'semestre', 'ano', 'ch']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_aluno = None

    def form_valid(self, form):
        self.id_aluno = form.instance.aluno.id_aluno
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listar_aproveitamento', kwargs={'pk': self.id_aluno})


class ExportarDados(View):
    def get(self, request, *args, **kwargs):

        data = []

        for aluno in Aluno.objects.all():
            for aproveitamento in Aproveitamento.objects.filter(aluno=aluno):
                linha = {'Aluno': aluno.nome, 'Código': aproveitamento.categoria,
                         'Atividade': aproveitamento.descricao, 'Carga Horária': aproveitamento.ch}
                data.append(linha)

        # Criar o DataFrame a partir dos dados
        df = pd.DataFrame(data)

        # Exportar o DataFrame como um arquivo Excel
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="dados.xlsx"'
        df.to_excel(response)

        return response
